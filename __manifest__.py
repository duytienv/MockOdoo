# -*- coding: utf-8 -*-

{
    'name': 'Mock Odoo',
    'summary': """
            BEER
        """,
    'description': """
        TASYS
    """,
    'data': [
        'wizard/test.xml',
        'views/template.xml',
        'report/baocao.xml',
        'views/ptd_broken.xml',
        'views/ptd_manager.xml',
        'views/ptd_manufactor.xml',
        'views/ptd_maintain_info.xml',
        'views/ptd_install_location.xml',
        'views/ptd_technical_characteristics.xml',
        'views/ptd_system.xml',
        'views/ptd_unit_manager.xml',
        'views/ptd_unit.xml',
        'views/ptd_year_format.xml',
        'views/ptd_ptd.xml',
        'views/ptd_check_or_correct.xml',
        'views/ptd_type_equip.xml',
        'views/ptd_device_group.xml',
        'views/menu.xml',
    ],
    'qweb': [

    ],
    'version': '0.1',
    'author': 'TASYS',
    'category': 'Viettel Corporation',
    'license': 'LGPL-3',
    'sequence': 1,
    'depends': ['base', 'mail','hr'],
    'installable': True,
    'application': True,
    'auto_install': False
}