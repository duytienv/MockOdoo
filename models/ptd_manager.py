# -*- coding: utf-8 -*-

from odoo import models, fields


class PtdManager(models.Model):
    _name = "ptd.manager"
    _description = "Manager"

    id = fields.Integer(string="Mã người quản lý", required=True)
    name = fields.Char(string="Tên người quản lý")
    unit_manager = fields.Many2one("ptd.unit.manager", string="Đơn vị quản lý")
    note = fields.Char(string="Ghi chú")
