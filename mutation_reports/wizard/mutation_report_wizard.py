from odoo import fields, models
from asyncio.log import logger
from datetime import datetime
from dateutil import relativedelta
from odoo import exceptions

class MutationReportWizard(models.TransientModel):
    _name = 'mutation.report.wizard'
    _description = 'Form Mutation report Wizard'

    start_date = fields.Date('Start Date', default=datetime.now().strftime('%Y-%m-01'))
    end_date = fields.Date('End Date', default=str(datetime.now() + relativedelta.relativedelta(months=+1, day=1, days=-1))[:10])
    categ_id = fields.Many2one('product.category', string='Product Category')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

    def print_report(self):
        ir_action_report = self.env['ir.actions.report']._get_report_from_name('mutation_reports.mutation_report_template')
            
        domain = []
        if self.categ_id:
            domain += [('categ_id','=', self.categ_id.id)]

        product_templates = self.env['product.template'].search(domain)
        stock_moves_lines = self.env['stock.move.line'].search([('date','>=', self.start_date), ('date','<=', self.end_date)])

        stock_moves_all = self.env['stock.move.line'].search([])
        stock_lalu = self.env['stock.sisa.lalu'].search([])  

        month = int(self.start_date.strftime('%m'))
        m1 = min(stock_moves_all.mapped('date'))
        m2 = self.start_date
        months = relativedelta.relativedelta(m2, m1)
        total_months = months.months
        for m in range(total_months+1):
            list_month = m1 + relativedelta.relativedelta(months=+m)
            list_month_res = int(list_month.strftime('%m'))
            month_lalu = list_month + relativedelta.relativedelta(months=-1)
            month_lalu_res = int(month_lalu.strftime('%m'))

            sisa_lalu = [{
                'product_id': rec.id,
                'sisa_akhir': int(((sum(sisa.sisa_akhir for sisa in stock_lalu.filtered(lambda s: int(s.bulan.strftime('%m')) == month_lalu_res and s.product_id.id == rec.id))+sum(lines.qty_done for lines in stock_moves_all.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal' and int(y.date.strftime('%m')) == list_month_res)))) - sum(lines.qty_done for lines in stock_moves_all.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal' and int(y.date.strftime('%m')) == list_month_res))) if min(stock_lalu.mapped('bulan')) else int(((sum(lines.qty_done for lines in stock_moves_all.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal' and int(y.date.strftime('%m')) == list_month_res)))) - sum(lines.qty_done for lines in stock_moves_all.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal' and int(y.date.strftime('%m')) == list_month_res))),
                'bulan': list_month
                } for rec in product_templates] 
            stock_lalu.create(sisa_lalu)
            
        if stock_lalu:
            stock_lalu.unlink()

        if product_templates:
            return ir_action_report.report_action(docids = product_templates.ids,
            data={
                'product_template':product_templates.ids,
                'start_date':self.start_date,
                'end_date':self.end_date,
                'company': self.company_id.name,
                'company_city': self.company_id.city,
            }) 
        else: 
            raise exceptions.ValidationError('Data Produk tidak ditemukan!')
    