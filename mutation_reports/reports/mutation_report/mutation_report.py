from odoo import models, _
from datetime import datetime
from asyncio.log import logger
from odoo import exceptions

class ReportMutation(models.AbstractModel):
    _name = 'report.mutation_reports.mutation_report_template'
    _description = 'ReportMutation'

    def _get_report_values(self, docids, data=None):
        Report = self.env['ir.actions.report']._get_report_from_name('mutation_reports.mutation_report_template')
        product_templates = self.env[Report.model].browse(data.get('product_template'))
        stock_moves_range = self.env['stock.move.line'].search([('date','>=', data['start_date']), ('date','<=', data['end_date'])])
        stock_moves_all = self.env['stock.move.line'].search([])

        bfr_month = int(min(stock_moves_range.mapped('date')).strftime('%m')) - 1
        
        sisa_lalu = [{
            'product_id': sisa.id,
            'product': sisa.name,
            'first_stock': 0,
            'stock_in': sum(lines.qty_done for lines in stock_moves_all.filtered(lambda y: y.product_id.id == sisa.id and y.location_id.usage != 'internal' and int(y.date.strftime('%m')) == bfr_month)),
            'stock_out': sum(lines.qty_done for lines in stock_moves_all.filtered(lambda y: y.product_id.id == sisa.id and y.location_id.usage == 'internal' and int(y.date.strftime('%m')) == bfr_month)),
            'sisa': sum(lines.qty_done for lines in stock_moves_all.filtered(lambda y: y.product_id.id == sisa.id and y.location_id.usage != 'internal' and int(y.date.strftime('%m')) == bfr_month)) - sum(lines.qty_done for lines in stock_moves_all.filtered(lambda y: y.product_id.id == sisa.id and y.location_id.usage == 'internal' and int(y.date.strftime('%m')) == bfr_month)),
        } for sisa in product_templates]


        products = [{
            'product_id': rec.id,
            'product': rec.name,
            'categ': rec.categ_id.id,
            'code': rec.default_code,
            'uom': rec.uom_id.name,
            'first_stock': int(sum(sisa['sisa'] for sisa in sisa_lalu if sisa['product_id'] == rec.id)),
            # 'first_stock': 0,
            'stock_in': int(sum(lines.qty_done for lines in stock_moves_range.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))),
            'stock_out': int(sum(lines.qty_done for lines in stock_moves_range.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))),
            'sisa': int((sum(sisa['sisa'] for sisa in sisa_lalu if sisa['product_id'] == rec.id) + sum(lines.qty_done for lines in stock_moves_range.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_range.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))),
            # 'sisa': int((sum(lines.qty_done for lines in stock_moves_range.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_range.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))),
            # 'month': int(min(stock_moves_range.mapped('date')).strftime('%m'))
        } for rec in product_templates]
        
        # logger.info(products)

        # www

        res = [cat['categ'] for cat in products]

        categ_ids = self.env['product.category'].search([('id','in', res)],order='name asc')
        return {
            'products': products,
            'categ': categ_ids,
            'start_date':datetime.strptime(data['start_date'],'%Y-%m-%d').strftime('%B %Y'),
            'company': data['company'],
            'company_city': data['company_city']
        }
