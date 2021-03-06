from odoo.tests.common import TransactionCase


class TestResPartner(TransactionCase):

    def setUp(self):
        super(TestResPartner, self).setUp()
        self.customer = self.env.ref('base.res_partner_3')

    def test_write(self):
        self.customer.update({'committee_position': 'ABC'})
