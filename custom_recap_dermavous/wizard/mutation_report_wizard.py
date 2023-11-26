from odoo import fields, models
from asyncio.log import logger
from datetime import datetime
from dateutil import relativedelta

class MutationReportWizard(models.TransientModel):
    _name = 'mutation.report.wizard'
    _description = 'Form Mutation report Wizard'

    start_date = fields.Date('Start Date', default=datetime.now().strftime('%Y-%m-01'))
    end_date = fields.Date('End Date', default=str(datetime.now() + relativedelta.relativedelta(months=+1, day=1, days=-1))[:10])
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

    def print_report(self):
        ir_action_report = self.env['ir.actions.report']._get_report_from_name('custom_recap_dermavous.mutation_report_template')
            
        product_templates = self.env['product.template'].search([])

        # www
        return ir_action_report.report_action(docids = product_templates.ids,
        data={
            'product_template':product_templates.ids,
            'start_date':self.start_date,
            'end_date':self.end_date,
            'company': self.company_id.name,
            'company_city': self.company_id.city,
        })
    