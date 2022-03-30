# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Fone Zone Quotation Report',
    'version': '1.0',
    'summary': 'Sale Quotation Pdf report',
    'sequence': 10,
    'description': """FoneZone Sale Quotation Report""",
    'category': 'sales',
    'website': 'https://www.mediodconsulting.com',
    'images': [],
    'depends': ['sale'],
    'data': [
        'reports/sale_quotation_report.xml',
        'reports/account_move_report.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}