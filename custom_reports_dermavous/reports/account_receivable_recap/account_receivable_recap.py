from odoo import models, api, _
from asyncio.log import logger

class AccountMoveRecap(models.AbstractModel):
    _name = 'report.custom_reports_dermavous.account_receivable_recap'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, invoice):

        # add format
        title_style = workbook.add_format({'bold':'True',})
        header_table_style = workbook.add_format({'align':'center','bold':True,'border': 1})
        body_table_tyle = workbook.add_format({'border': 1,'align': 'center'})
        body_table_tyle_idr = workbook.add_format({'border': 1,'align': 'right'})
        body_table_tyle_else = workbook.add_format({'border': 1,'align': 'center', 'color': 'red'})


        row = 0
        col = 0

        sheet = workbook.add_worksheet("Rekap Faktur Akun Piutang Usaha")
        sheet.set_column('B:B', 23)
        sheet.set_column('C:C', 35)
        sheet.set_column('D:D', 25)
        sheet.set_column('E:E', 32)
        sheet.set_column('F:F', 20)
        sheet.set_column('G:G', 20)

        row += 0
        sheet.merge_range(row, col, row, col + 2, "Rekap Faktur Akun Piutang Usaha", title_style)
        row += 1
        sheet.merge_range(row, col, row, col + 2, invoice.company_id.name, title_style)

        row += 2

        sheet.write(row, col, "NO", header_table_style)
        sheet.write(row, col + 1, "NO FAKTUR", header_table_style)
        sheet.write(row, col + 2, "NAMA PELANGGAN", header_table_style)
        sheet.write(row, col + 3, "TANGGAL FAKTUR", header_table_style)
        sheet.write(row, col + 4, "AKUN", header_table_style)
        sheet.write(row, col + 5, "NOMINAL", header_table_style)
        sheet.write(row, col + 6, "SISA", header_table_style)

        for no, inv in enumerate(invoice):
            row += 1
            sheet.write(row, col, no+1, body_table_tyle)
            sheet.write(row, col + 1, inv.name, body_table_tyle)
            sheet.write(row, col + 2, inv.partner_id.name, body_table_tyle)
            sheet.write(row, col + 3, inv.invoice_date.strftime('%d %B %Y'), body_table_tyle)
            for account in inv.line_ids.filtered(lambda u: u.date_maturity and u.debit):
                if account.account_id.name == 'Piutang Usaha' or account.account_id.name == 'Account Receivable':
                    sheet.write(row, col + 4, "{} - {}".format(account.account_id.code, account.account_id.name), body_table_tyle) 
                else: 
                    sheet.write(row, col + 4, "{} - {}".format(account.account_id.code, account.account_id.name), body_table_tyle_else) 

                sheet.write(row, col + 5, '{:,.0f}'.format(account.debit), body_table_tyle_idr)
                sheet.write(row, col + 6, '{:,.0f}'.format(account.amount_residual), body_table_tyle_idr)



            

