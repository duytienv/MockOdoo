from odoo import models, fields, api


class PtdSystem(models.Model):
    _name = "ptd.system"
    _description = "Thông tin hệ thống"
    _rec_name = "sys_id"
    _sql_constraints = [('sys_id','unique(sys_id)','Mã hệ thống đã tồn tại'), ]

    # id = fields.Char(string="ID")
    sys_id = fields.Text(string="Mã hệ thống")
    name = fields.Text(string="Tên hệ thống")
    unit_manager_id = fields.Many2one('ptd.unit.manager')
    note = fields.Char(string="Note")
