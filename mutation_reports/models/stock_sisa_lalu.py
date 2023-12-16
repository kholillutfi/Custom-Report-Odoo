from odoo import fields, models

class StockSisaLalu(models.Model):
    _name = 'stock.sisa.lalu'
    _description = 'Tabel Stock Sisa Lalu'

    product_id = fields.Many2one('product.template', string='product')
    sisa_akhir = fields.Integer(string='Sisa Akhir')
    bulan = fields.Date('bulan')
    