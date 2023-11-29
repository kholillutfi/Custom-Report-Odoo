from odoo import models, _
from datetime import datetime
from asyncio.log import logger

class ReportMutation(models.AbstractModel):
    _name = 'report.custom_recap_dermavous.mutation_report_template'
    _description = 'ReportMutation'

    def _get_report_values(self, docids, data=None):
        Report = self.env['ir.actions.report']._get_report_from_name('custom_recap_dermavous.mutation_report_template')
        product_templates = self.env[Report.model].browse(data.get('product_template'))
        stock_moves_lines = self.env['stock.move.line'].search([]).filtered(lambda t: t.product_id.id in product_templates.ids)

        products = [{
            'product': rec.name,
            'categ': rec.categ_id.id,
            'code': rec.default_code,
            'uom': rec.uom_id.name,
            'stock_date_1': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1))),
            'stock_in': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))),
            'stock_out': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))),
            'sisa': int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) if int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) > 1 else 0,
        } for rec in product_templates]

        res = [cat['categ'] for cat in products]
        # logger.info(res)

        categ_ids = self.env['product.category'].search([('id','in', res)],order='name asc')

        return {
            'products': products,
            'categ': categ_ids,
            'start_date':datetime.strptime(data['start_date'],'%Y-%m-%d').strftime('%B %Y'),
            'company': data['company'],
            'company_city': data['company_city']
        }
