from odoo import models, fields, api
from odoo.exceptions import UserError

class PtdBroken(models.Model):
    _name = "ptd.broken"
    _description = "Lịch sử hỏng"

    fail_time = fields.Date(string="Ngày hỏng", require = True)
    fail_reason =fields.Text(string="Nguyên nhân hỏng", require = True)
    broken_id=fields.Many2one("ptd.ptd")

    @api.model
    def create(self, vals):
        if vals['fail_time']==0 or vals['fail_reason']==0:
            raise UserError(
                "Thêm đầy đủ ngày, nguyên nhân hỏng")
        else:
            result = super(PtdBroken, self).create(vals)
        return result
    def write(self, vals):
        if 'fail_time' in vals:
            # print(vals['fail_time'])
            if vals['fail_time']==False:
                raise UserError(
                    "Thêm đầy đủ ngày, nguyên nhân hỏng")
        elif 'fail_reason' in vals:
            if vals['fail_reason']==False:
                raise UserError(
                    "Thêm đầy đủ ngày, nguyên nhân hỏng")
        result = super(PtdBroken, self).write(vals)
        return result