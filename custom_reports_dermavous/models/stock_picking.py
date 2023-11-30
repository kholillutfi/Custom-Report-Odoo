from odoo import fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    po_eksternal_number = fields.Char('No. Po (Eksternal)') 




