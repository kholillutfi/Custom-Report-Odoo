from odoo import models, fields, api
from asyncio.log import logger

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    
    def find_index(self, field_tax):
        taxes = [y[1] for y in field_tax]
        res = sum(tax for tax in taxes)
        return res
