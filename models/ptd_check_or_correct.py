from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime, timedelta
class PtdCheckOrCorrect(models.Model):
    _name = "ptd.check.or.correct"
    _description = "Kiểm định hiệu chỉnh"

    id=fields.Char("ID")
    name = fields.Selection(
        string='Kết quả',
        selection=[('1', 'Pass'), ('2', 'Fail')],
        tracking=True
    )
    stand_link_type = fields.Selection(
        string='Loại liên kết chuẩn',
        selection=[('1', 'Kiểm định'), ('2', 'Hiệu chỉnh'),('3','Kiểm tra kỹ thuật đo lường')],
        tracking=True
    )
    implementation_date=fields.Date(string="Ngày thực hiện", require=True)
    validity_date = fields.Date(string="Ngày hiệu lực theo GCN")
    expiry_date = fields.Date("Ngày hết hạn theo GCN")
    organisation_id = fields.Char(string="Đơn vị chứng nhận")
    reason_not_pass = fields.Char(string="Nguyên nhân không đạt")
    certificate_number = fields.Char(string="Số giấy chứng nhận")
    certificate = fields.Binary(string="Giấy chứng nhận")
    performer = fields.Char(string="Người thực hiện")
    note = fields.Text(string = 'Note')
    check_or_correct_id= fields.Many2one(comodel_name='ptd.ptd')

    @api.onchange('validity_date')
    def _expiry_date(self):
        if self.validity_date:
            self.expiry_date=self.validity_date + timedelta(days=180)
    @api.model
    def create(self, vals):
        if vals['name'] == 0:
            raise UserError("Kết quả không được để trống")
        if vals['stand_link_type'] == 0:
            raise UserError("Loại liên kết chuẩn không được để trống")
        if vals['organisation_id'] == 0:
            raise UserError("Đơn vị chứng nhận không được để trống")
        if vals['name']=='2':
            if vals['reason_not_pass'] == 0:
                raise UserError("Nguyên nhân không đạt không được để trống")
        if vals['certificate_number'] == 0:
            raise UserError("Số giấy chứng nhận không được để trống")
        if vals['certificate_number'].isalnum() == False:
            raise UserError("Số giấy chứng nhận chỉ gồm ký tự và số")
        if vals['certificate'] == 0:
            raise UserError("Giấy chứng nhận không được để trống")
        if vals['validity_date'] == 0:
            raise UserError("Ngày hiệu lực theo GCN không được để trống")
        if vals['implementation_date']==0:
            raise UserError("Ngày thực hiện không được để trống")
        if vals['stand_link_type'] == 0:
            raise UserError("Loại liên kết chuẩn không được để trống")


        #điều kiện tạo ngày thực hiện, hiệu lực, hết hạn
        if vals['implementation_date']>vals['validity_date']:
            raise UserError("Ngày hiệu lực không hợp lệ")
        else:
            result = super(PtdCheckOrCorrect, self).create(vals)
        return result

    def write(self, vals):
        #update các trường không được để thiếu
        if 'stand_link_type' in vals:
            # print(vals['stand_link_type'])
            if vals['stand_link_type'] ==False:
                raise UserError("Loại liên kết chuẩn không được để trống")
        if 'organisation_id' in vals:
            print(vals['organisation_id'])
            if len(vals['organisation_id']) == 0:
                raise UserError("Đơn vị chứng nhận không được để trống")

        if 'certificate_number' in vals:
            if len(vals['certificate_number'])==0:
                raise UserError("Số giấy chứng nhận không được để trống")
            else:
                if vals['certificate_number'].isalnum() == False:
                    raise UserError("Số giấy chứng nhận chỉ gồm ký tự và số")

        if 'certificate' in vals:
            # print(vals['certificate'])
            if len(vals['certificate']) == 0:
                raise UserError("Giấy chứng nhận không được để trống")
        if 'reason_not_pass' in vals:
            if len(vals['reason_not_pass']) == 0:
                raise UserError("Nguyên nhân không đạt không được để trống")

        #update thời gian thực hiện, sử dụng, hết hạn
        date1= self.implementation_date
        date2 = self.validity_date
        if 'implementation_date' in vals:
            date1=vals['implementation_date']
        if 'validity_date' in vals:
            date2=vals['validity_date']

        if datetime.strptime(str(date1),"%Y-%m-%d").date() >= datetime.strptime(str(date2),"%Y-%m-%d").date():
            raise UserError("Ngày hiệu lực không hợp lệ")


        # update nguyên nhân không đạt
        if 'name' in vals:
            if vals['name'] == False:
                raise UserError("Kết quả không được để trống")
            if vals['name'] == '2' and 'reason_not_pass' not in vals:
                raise UserError("Nguyên nhân không đạt không được để trống")
        result = super(PtdCheckOrCorrect, self).write(vals)
        return result