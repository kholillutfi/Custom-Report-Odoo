from odoo import api, fields, models
from datetime import datetime

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    jml_box = fields.Integer(string='Jml Box')
    note = fields.Char(string='Note')
    netto = fields.Char('Netto')