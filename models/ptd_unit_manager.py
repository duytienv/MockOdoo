from odoo import models, fields, api
class PtdUnitManager(models.Model):
    _name = "ptd.unit.manager"
    _description = "Đơn vị quản lý"

    id = fields.Char(string="Id")
    name = fields.Text(string="Đơn vị quản lý ")
    type= fields.Selection(
        string='Chọn đơn vị',
        selection=[('1', 'Đơn vị quản lý cấp 1'), ('2', 'Đơn vị quản lý cấp 2'), ('3', 'Đơn vị quản lý trực tiếp')],
        default='1',
        tracking=True
    )
    note = fields.Text(string="Note")
    unit_manager_id = fields.Many2one("ptd.system")