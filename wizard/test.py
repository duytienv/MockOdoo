from odoo import fields, models, api

class Test(models.TransientModel):
    _name = "test"
    asset_code = fields.Integer(string="Mã QLTS")
    def test(self):
        while(self.total_fees<1000):
            print(self.total_fees, "TÔI YÊU EM")
            self.total_fees+=1
        return True

    def search_view(self):
        action = self.env.ref('Mock_odoo.ptd_ptd_act').read()[0]
        action['domain'] = [('asset_code', '=', self.asset_code)]
        print(action)
        return action
