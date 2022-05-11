# -*- coding: utf-8 -*-

from odoo import models, fields


class PtdMaintainInfo(models.Model):
    _name = "ptd.maintain.info"
    _description = "Maintain Information"

    id = fields.Integer(string="Mã ", required=True)
    name = fields.Char(string="Người thực hiện")
    cost = fields.Char(string="Giá thành")
    implementation_date = fields.Date(string="Ngày thực hiện")
    attach_file = fields.Char(string="File đính kèm")
    note = fields.Char(string="Ghi chú")
    maintain_info_id=fields.Many2one("ptd.ptd")
