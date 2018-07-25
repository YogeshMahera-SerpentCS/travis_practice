# -*- coding: utf-8 -*-
# Copyright 2018 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Committees For Community Portal',
    'category': 'website',
    'summary': 'Committees management',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'website': 'www.serpentcs.com',
    'depends': [
        'website_community_portal',
    ],
    'data': [
        'security/portal_security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu_details.xml',
        'views/res_partner_view.xml',
        'views/job_assign_view.xml',
        'views/template_committee_chart.xml',
        'views/template_committee_grid.xml'
    ],
    'installable': True,
    'application': True,
}
