# -*- coding: utf-8 -*-

from odoo import models, fields,api
from odoo.exceptions import UserError

class PtdMaintainInfo(models.Model):
    _name = "ptd.maintain.info"
    _description = "Maintain Information"

    name = fields.Char(string="Người thực hiện")
    cost = fields.Char(string="Giá thành")
    implementation_date = fields.Date(string="Ngày thực hiện")
    attach_file = fields.Binary(string="File đính kèm")
    note = fields.Char(string="Ghi chú")
    maintain_info_id=fields.Many2one("ptd.ptd")
    @api.model
    def create(self, vals):
        if vals['implementation_date'] == 0:
            raise UserError("Ngày thực hiện không được để trống")
        elif vals['note'] == 0:
            raise UserError("Ghi chú không được để trống")
        elif vals['attach_file']==0:
            raise UserError("File không được để trống")
        else:
            result = super(PtdMaintainInfo, self).create(vals)
        return result

    def write(self, vals):
        if 'implementation_date' in vals:
            print(vals['implementation_date'])
            if vals['implementation_date'] == False:
                raise UserError("Ngày thực hiện không được để trống")

        if 'note' in vals:
            print(vals['note'])
            if vals['note'] == False:
                raise UserError("Ghi chú không được để trống")

        if 'attach_file' in vals:
            print(vals['attach_file'])
            if vals['attach_file'] == False:
                raise UserError("File đính kèm không được để trống")

        result = super(PtdMaintainInfo, self).write(vals)
        return result


