from odoo import models, fields, api

class PtdUnit(models.Model):
    _name = "ptd.unit"
    _description = "Đơn vị tính"

    # id = fields.Char(string="Id")
    name = fields.Text(string="Đơn vị tính")
    note = fields.Char(string="Note")

