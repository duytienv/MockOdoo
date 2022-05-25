from odoo import fields, models
from odoo.exceptions import UserError
class Test(models.TransientModel):
    _name = "ptd.timkiem"
    commodity_code = fields.Char(string="Mã thiết bị")
    name_device = fields.Char(string="Tên thiết bị")
    status=fields.Selection(
        string='Tình trạng KĐ/HC',
        selection=[('2', 'Tất cả'),
                   ('1', 'Đã KĐ/HC'),
                   ('0', 'Chưa KĐ/HC')],
        tracking=True
    )

    maintain = fields.Selection(
        string='Tình trạng BD',
        selection=[('2', 'Tất cả'),
                   ('1', 'Đã BD'),
                   ('0', 'Chưa BD')],
        tracking=True
    )

    type_of = fields.Selection(
        string='Loại KĐ/HC',
        selection=[('2', 'Tất cả'),
                   ('1', 'Kiểm định'),
                   ('0', 'Hiệu chỉnh')],
        tracking=True
    )
    def search_view(self):
        # search = []
        # if self.commodity_code or self.name_device:
        #     search.append(('commodity_code','ilike',self.commodity_code))
        #     search.append(('name', 'ilike', self.name_device))
        #     search.append(('check_or_correct', 'ilike', self.status))
        # if search:
        #     partner = self.env['ptd.ptd'].search(search)
        #     if not partner:
        #         raise UserError("Không có thiết bị thỏa mãn")

        domain= [('commodity_code', 'ilike', self.commodity_code),
                       ('name', 'ilike', self.name_device) ]
        if self.status!='2':
            domain.append(('check_or_correct', 'ilike', self.status))

        if self.maintain != '2':
            domain.append(('maintain_info', 'ilike', self.maintain))
        if self.type_of != '2':
            domain.append(('type_of', 'ilike', self.type_of))
        partner = self.env['ptd.ptd'].search(domain)
        if not partner:
            raise UserError('Không có thiết bị thỏa mãn')
        return {
            'name': ('Tìm kiếm thiết bị'),
            'view_mode': 'tree',
            'views': [(self.env.ref('mock_odoo1.action_ptd_ptd_tree').id, 'tree'),
                      (self.env.ref('mock_odoo1.view_ptd_ptd_form').id, 'form')],
            'view_id': False,
            'domain': domain,
            'res_model': 'ptd.ptd',
            'type': 'ir.actions.act_window',
            'current': 'new',
        }
