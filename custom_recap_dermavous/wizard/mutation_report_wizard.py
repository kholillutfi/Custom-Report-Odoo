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
        ir_action_report = self.env['ir.actions.report']._get_report_from_name('custom_recap_dermavous.mutation_report_template')
        stock_moves_lines = self.env['stock.move.line'].search([('date','>=', self.start_date), ('date','<=', self.end_date)])
            
        domain = []
        if self.categ_id:
            domain += [('categ_id','=', self.categ_id.id)]


        product_templates = self.env['product.template'].search(domain)

        if product_templates:
            product_filter = product_templates.filtered(lambda e: e.id in stock_moves_lines.mapped('product_id').ids)
            logger.info(product_templates.mapped('id'))
            logger.info(stock_moves_lines.mapped('product_id').mapped('id'))    
            if product_filter:
                return ir_action_report.report_action(docids = product_filter.ids,
                data={
                    'product_template':product_filter.ids,
                    'start_date':self.start_date,
                    'end_date':self.end_date,
                    'company': self.company_id.name,
                    'company_city': self.company_id.city,
                }) 
            else: 
                raise exceptions.ValidationError('Produk {} Tidak ada Data Pergerakan Produk!'.format(', '.join(product_templates.mapped('name'))))   
        else: 
            raise exceptions.ValidationError('Data Produk tidak ditemukan!')
    