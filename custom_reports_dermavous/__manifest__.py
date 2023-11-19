# -*- coding: utf-8 -*-
{
    'name': "Custom Reports - Dermavous",

    'summary': """
        General Features
        - Delivery Letter Report 
        - Invoice Deu
        """,

    'description': """
        Environment Variables
        - None

        Configuration needed to use features 
        - None

        Created on:
        - Created on 05 November 2023
    """,

    'author': "M. Kholil Lutfi",
    'company': 'PT. Cendana Teknika Utama',
    'category': 'Reporting',
    'version': '14.0.0.1',
    'sequence': 1,
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'LGPL-3', 

    # any module necessary for this one to work correctly
    'depends': ['base','stock','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/stock_picking_views.xml',
        'views/stock_move_line_views.xml',
        'reports/delivery_letter_reports/delivery_letter_report_paperformat.xml',
        'reports/delivery_letter_reports/delivery_letter_report_template.xml',
        'reports/delivery_letter_reports/delivery_letter_report_actions.xml',
        'reports/invoice_deu_reports/invoice_deu_report_paperformat.xml',
        'reports/invoice_deu_reports/invoice_deu_report_template.xml',
        'reports/invoice_deu_reports/invoice_deu_report_actions.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
