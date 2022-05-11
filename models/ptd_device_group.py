from odoo import models, fields, api
class PtdDeviceGroup(models.Model):
    _name = "ptd.device.group"
    _description = "Device group manegement"

    id = fields.Char("ID")

    name = fields.Char(string = 'Device Group *', required = True)
    note = fields.Text(string = 'Note')