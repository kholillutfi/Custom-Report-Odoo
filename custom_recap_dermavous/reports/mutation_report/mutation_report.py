from odoo import models, _
from datetime import datetime
from asyncio.log import logger

class ReportMutation(models.AbstractModel):
    _name = 'report.custom_recap_dermavous.mutation_report_template'
    _description = 'ReportMutation'

    def _get_report_values(self, docids, data=None):
        Report = self.env['ir.actions.report']._get_report_from_name('custom_recap_dermavous.mutation_report_template')
        stock_moves_lines = self.env['stock.move.line'].search([('date','>=', data['start_date']), ('date','<=', data['end_date'])])
        product_templates = self.env[Report.model].browse(data.get('product_template'))

        products_categ_all = [{
            'product': rec.name,
            'code': rec.default_code,
            'uom': rec.uom_id.name,
            'stock_date_1': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1))),
            'stock_in': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))),
            'stock_out': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))),
            'sisa': int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) if int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) > 1 else 0,
        } for rec in product_templates.filtered(lambda e: e.id in stock_moves_lines.mapped('product_id').mapped('id') and e.categ_id.id == self.env.ref('product.product_category_all').id)]

        products_categ_1 = [{
            'product': rec.name,
            'code': rec.default_code,
            'uom': rec.uom_id.name,
            'stock_date_1': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1))),
            'stock_in': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))),
            'stock_out': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))),
            'sisa': int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) if int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) > 1 else 0,
        } for rec in product_templates.filtered(lambda e: e.id in stock_moves_lines.mapped('product_id').mapped('id') and e.categ_id.id == self.env.ref('product.product_category_1').id)]

        products_categ_2 = [{
            'product': rec.name,
            'code': rec.default_code,
            'uom': rec.uom_id.name,
            'stock_date_1': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1))),
            'stock_in': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))),
            'stock_out': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))),
            'sisa': int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) if int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) > 1 else 0,
        } for rec in product_templates.filtered(lambda e: e.id in stock_moves_lines.mapped('product_id').mapped('id') and e.categ_id.id == self.env.ref('product.product_category_2').id)]

        products_categ_3 = [{
            'product': rec.name,
            'code': rec.default_code,
            'uom': rec.uom_id.name,
            'stock_date_1': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1))),
            'stock_in': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))),
            'stock_out': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))),
            'sisa': int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) if int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) > 1 else 0,
        } for rec in product_templates.filtered(lambda e: e.id in stock_moves_lines.mapped('product_id').mapped('id') and e.categ_id.id == self.env.ref('product.product_category_3').id)]

        products_categ_4 = [{
            'product': rec.name,
            'code': rec.default_code,
            'uom': rec.uom_id.name,
            'stock_date_1': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1))),
            'stock_in': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))),
            'stock_out': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))),
            'sisa': int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) if int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) > 1 else 0,
        } for rec in product_templates.filtered(lambda e: e.id in stock_moves_lines.mapped('product_id').mapped('id') and e.categ_id.id == self.env.ref('product.product_category_4').id)]

        products_categ_5 = [{
            'product': rec.name,
            'code': rec.default_code,
            'uom': rec.uom_id.name,
            'stock_date_1': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1))),
            'stock_in': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))),
            'stock_out': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))),
            'sisa': int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) if int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) > 1 else 0,
        } for rec in product_templates.filtered(lambda e: e.id in stock_moves_lines.mapped('product_id').mapped('id') and e.categ_id.id == self.env.ref('product.product_category_5').id)]

        products_categ_6 = [{
            'product': rec.name,
            'code': rec.default_code,
            'uom': rec.uom_id.name,
            'stock_date_1': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1))),
            'stock_in': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))),
            'stock_out': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))),
            'sisa': int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) if int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) > 1 else 0,
        } for rec in product_templates.filtered(lambda e: e.id in stock_moves_lines.mapped('product_id').mapped('id') and e.categ_id.id == self.env.ref('product.product_category_6').id)]

        products_categ_cat_expense = [{
            'product': rec.name,
            'code': rec.default_code,
            'uom': rec.uom_id.name,
            'stock_date_1': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1))),
            'stock_in': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))),
            'stock_out': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))),
            'sisa': int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) if int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) > 1 else 0,
        } for rec in product_templates.filtered(lambda e: e.id in stock_moves_lines.mapped('product_id').mapped('id') and e.categ_id.id == self.env.ref('product.cat_expense').id)]

        products_categ_consumable = [{
            'product': rec.name,
            'code': rec.default_code,
            'uom': rec.uom_id.name,
            'stock_date_1': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1))),
            'stock_in': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))),
            'stock_out': int(sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))),
            'sisa': int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) if int((sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda r: r.product_id.id == rec.id and int(r.date.strftime('%d')) == 1)) + sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage != 'internal'))) - sum(lines.qty_done for lines in stock_moves_lines.filtered(lambda y: y.product_id.id == rec.id and y.location_id.usage == 'internal'))) > 1 else 0,
        } for rec in product_templates.filtered(lambda e: e.id in stock_moves_lines.mapped('product_id').mapped('id') and e.categ_id.id == self.env.ref('product.product_category_consumable').id)]

        # logger.info(products_categ_all)
        # www

        return {
            'product_all': products_categ_all,
            'product_categ_1': products_categ_1,
            'product_categ_2': products_categ_2,
            'product_categ_3': products_categ_3,
            'product_categ_4': products_categ_4,
            'product_categ_5': products_categ_5,
            'product_categ_6': products_categ_6,
            'product_categ_cat_expense': products_categ_cat_expense,
            'product_categ_consumable': products_categ_consumable,
            'product_all_id': self.env.ref('product.product_category_all').name,
            'product_categ_1_id': self.env.ref('product.product_category_1').name,
            'product_categ_2_id': self.env.ref('product.product_category_2').name,
            'product_categ_3_id': self.env.ref('product.product_category_3').name,
            'product_categ_4_id': self.env.ref('product.product_category_4').name,
            'product_categ_5_id': self.env.ref('product.product_category_5').name,
            'product_categ_6_id': self.env.ref('product.product_category_6').name,
            'product_categ_cat_expense_id': self.env.ref('product.cat_expense').name,
            'product_categ_consumable_id': self.env.ref('product.product_category_consumable').name,
            'start_date':datetime.strptime(data['start_date'],'%Y-%m-%d').strftime('%B %Y'),
            'company': data['company'],
            'company_city': data['company_city']
        }
