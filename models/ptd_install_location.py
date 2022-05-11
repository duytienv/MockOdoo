# -*- coding: utf-8 -*-
from odoo import models, fields
class PtdInstallLocation(models.Model):
    _name = "ptd.install.location"
    _description = "Install Location"

    id = fields.Integer(string="Mã Vị trí cài đặt", required=True)
    name = fields.Char(string="Vị trí lắp đặt")
    note = fields.Char(string="Ghi chú")
