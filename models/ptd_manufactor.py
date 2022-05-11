# -*- coding: utf-8 -*-

from odoo import models, fields


class PtdInstallLocation(models.Model):
    _name = "ptd.manufactor"
    _description = "Manufactor"

    id = fields.Integer(string="Mã nhà sản xuất", required=True)
    name = fields.Char(string="Nhà sản xuất")
    note = fields.Char(string="Ghi chú")
