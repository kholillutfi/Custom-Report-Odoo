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

        month = int(min(stock_moves_lines.mapped('date')).strftime('%m'))

        move_all = [{
            'date': rec.date.strftime('%m')
        }for rec in stock_moves_all]
        
        date = [rec['date'] for rec in move_all]

        month_set = list(set(date))
        int_month = [eval(e) for e in month_set]

        sorted_month = sorted(int_month, key=lambda x: x)

        for bfr_month in sorted_month:
            if bfr_month != month:
                month_sisa_lalu = bfr_month - 1        
                sisa_lalu = [{
                    'product_id': rec.id,
                    'sisa_akhir': int(((sum(sisa.sisa_akhir for sisa in stock_lalu.filtered(lambda s: s.month == month_sisa_lalu and s.product_id.id == rec.id))+sum(lines.qty_done for lines in stock_moves_all.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal' and int(y.date.strftime('%m')) == bfr_month)))) - sum(lines.qty_done for lines in stock_moves_all.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal' and int(y.date.strftime('%m')) == bfr_month))),
                    'month': bfr_month
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
    