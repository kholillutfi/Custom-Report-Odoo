# -*- coding: utf-8 -*-
{
    'name': "Custom Recap - Dermavous",

    'summary': """
        General Features
        - Account Receivable Invoice Recap
        """,

    'description': """
        Environment Variables
        - None

        Configuration needed to use features 
        - None

        Created on:
        - Created on 19 November 2023
    """,

    'author': "M. Kholil Lutfi",
    'company': 'PT. Cendana Teknika Utama',
    'category': 'Recap',
    'version': '16.0.0.1',
    'sequence': 1,
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'LGPL-3', 

    # any module necessary for this one to work correctly
    'depends': ['base','account','report_xlsx'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/account_receivable_recap/account_receivable_recap_action.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
