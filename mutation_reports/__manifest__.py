# -*- coding: utf-8 -*-
{
    'name': "Mutation Reports",

    'summary': """
        General Features
        - Mutation Reports by filter date range
        """,

    'description': """
        Environment Variables
        - None

        Configuration needed to use features 
        - None

        Created on:
        - Created on 09 Desember 2023
    """,

    'author': "M. Kholil Lutfi",
    'company': 'PT. Cendana Teknika Utama',
    'category': 'Accounting',
    'version': '16.0.0.1',
    'sequence': 1,
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'LGPL-3', 

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/mutation_report_views.xml',
        'wizard/mutation_report_actions.xml',
        'reports/mutation_report/mutation_report_template.xml',
        'reports/mutation_report/mutation_report_paperformat.xml',
        'reports/mutation_report/mutation_report_action.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
