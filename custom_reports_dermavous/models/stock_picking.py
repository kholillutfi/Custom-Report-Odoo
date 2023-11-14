from odoo import fields, models
from datetime import timedelta

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    po_eksternal_number = fields.Char('No. Po (Eksternal)') 

    def calculate_date(self, day_num):
        for rec in self.move_line_ids_without_package:
            if rec.lot_id:
                res = rec.lot_id.create_date + timedelta(days=day_num)
        
                return res
            
    



