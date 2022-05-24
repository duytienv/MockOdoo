from odoo import fields, models
from odoo.exceptions import UserError
class Test(models.TransientModel):
    _name = "ptd.timkiem"
    asset_code = fields.Text(string="Mã QLTS")
    name_device = fields.Char(string="Tên thiết bị")
    def search_view(self):
        search = []
        if self.asset_code:
            search.append(('asset_code','ilike',self.asset_code))
        if self.name_device:
            search.append(('name', 'ilike', self.name_device))
        if search:
            partner = self.env['ptd.ptd'].search(search)
            if not partner:
                raise UserError("Không có thiết bị thỏa mãn")
        return {
            'name': ('Tìm kiếm thiết bị'),
            'view_mode': 'tree',
            'views': [(self.env.ref('Mock_odoo.action_ptd_ptd_tree').id, 'tree'),
                      (self.env.ref('Mock_odoo.view_ptd_ptd_form').id, 'form')],
            'view_id': False,
            'domain': [('asset_code', 'ilike', self.asset_code),('name','ilike',self.name_device)],
            'res_model': 'ptd.ptd',
            'type': 'ir.actions.act_window',
            'current': 'new',
        }

