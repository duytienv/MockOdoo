from odoo import models, fields
class PtdTypeEquipment(models.Model):
    _name = "ptd.type.equip"
    _description = "Type of equipment management"

    id = fields.Char("ID")
    name = fields.Char(string='Chủng loại', required = True)
    number = fields.Integer(string='Số lượng', required=True)
    device_group_id = fields.Many2one(
        string = 'Nhóm',
        comodel_name ='ptd.device.group',
        required = True,
        ondelete = 'restrict'
    )
    note = fields.Text(string='Note')
