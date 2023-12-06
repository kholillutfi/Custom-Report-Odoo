from odoo import models, _
from datetime import datetime
from asyncio.log import logger

class ReportMutation(models.AbstractModel):
    _name = 'report.custom_recap_dermavous.mutation_report_template'
    _description = 'ReportMutation'

    def _get_report_values(self, docids, data=None):
        Report = self.env['ir.actions.report']._get_report_from_name('custom_recap_dermavous.mutation_report_template')
        product_templates = self.env[Report.model].browse(data.get('product_template'))
        stock_moves_lines = self.env['stock.move.line'].search([('date','>=', data['start_date']), ('date','<=', data['end_date'])])

        bfr_month = int(min(stock_moves_lines.mapped('date')).strftime('%m')) - 1
        
        stock_lalu = self.env['stock.sisa.lalu'].search([])

        products = [{
            'product': rec.name,
            'categ': rec.categ_id.id,
            'code': rec.default_code,
            'uom': rec.uom_id.name,
            'stock_date_1': sum(sisa.sisa_akhir for sisa in stock_lalu.filtered(lambda s: s.month == bfr_month and s.product_id.id == rec.id)),
            'stock_in': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))),
            'stock_out': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))),
            'sisa': int((sum(sisa.sisa_akhir for sisa in stock_lalu.filtered(lambda s: s.month == bfr_month and s.product_id.id == rec.id)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) if int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) > 1 else 0,
        } for rec in product_templates]

        res = [cat['categ'] for cat in products]

        categ_ids = self.env['product.category'].search([('id','in', res)],order='name asc')
        
        return {
            'products': products,
            'categ': categ_ids,
            'start_date':datetime.strptime(data['start_date'],'%Y-%m-%d').strftime('%B %Y'),
            'company': data['company'],
            'company_city': data['company_city']
        }
