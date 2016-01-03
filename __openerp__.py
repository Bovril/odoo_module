# -*- coding: utf-8 -*-
{
    'name': "HR Recruiting",

    'summary': """
        Module for recuirting""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Dudulez",
    'website': "http://www.dudulez.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/recruiting.xml',
        'views/recruiting_workflows.xml',
        'views/employee.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}