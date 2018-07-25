# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Community Portal',
    'version': '10.0.1.0.0',
    'author': 'Serpent Consulting Services PVT. LTD.',
    'category': 'Website',
    'license': 'AGPL-3',
    'website': 'http://www.serpentcs.com',
    'summary': ''' Website Matrimonial odoo.''',
    'depends': [
        'website',
        'sales_team',
        'website_menu_by_user_status',
        'website_blog_configurator',
        'website_portal_enhanced',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/res_country_state_data.xml',
        'data/res_city_data.xml',
        'data/education_data.xml',
        'data/height_data.xml',
        'views/master_view.xml',
        'views/res_city_view.xml',
        'views/res_partner_view.xml',
        'views/web_news.xml',
        'views/assets.xml',
        'views/account_details_view.xml',
        'views/homepage.xml',
        'views/templates.xml',
        'views/menu_details.xml',
    ],
    'qweb': ['static/src/xml/website_ace_inherited.xml'],
    'installable': True,
    'application': True,
}
