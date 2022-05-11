from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
import time
from datetime import datetime
class PhuongTienDo(models.Model):
    _name = "ptd.ptd"
    _description = "Create measuring device"


    # THÔNG TIN CHUNG


    asset_code = fields.Char("Mã QLTS", required = True)

    classify = fields.Selection(
        string='Phân loại',
        selection=[('1', 'Thiết bị chính'), ('2', 'Thiết bị phụ')],
        tracking=True,
        required = True
    )
    type_equip_id = fields.Many2one("ptd.type.equip", "Chủng loại thiết bị")

    device_group_id = fields.Many2one("ptd.device.group", "Nhóm thiết bị")

    model = fields.Text("Ký hiệu")

    system_id = fields.Many2one("ptd.system",string="Mã hệ thống")

    manufactor_id = fields.Many2one("ptd.manufactor",string="Nhà sản xuất")

    serial_number = fields.Text("Số hiệu", required =True)

    unit_id = fields.Many2one("ptd.unit", string="Đơn vị tính")

    country_id = fields.Many2one("res.country", "Nước sản xuất")

    year_manufacture = fields.Date('Năm sản xuất')

    year_use = fields.Date(string="Năm đưa vào sử dụng")

    img = fields.Image("IMG")

    description = fields.Text(string="Mô tả")

    attach_file = fields.Binary("Tài liệu kỹ thuật")

    defense_ministry_equipment = fields.Boolean(string="Trang bị đo lường tiêu chuẩn")

    # THÔNG TIN QUẢN LÝ

    manager_id = fields.Many2one("ptd.manager",string="Người quản lý trực tiếp")

    unit_manager_id = fields.Many2one('ptd.unit.manager',string="Đơn vị quản lý trực tiếp")

    handover_report = fields.Binary(string="Biên bản bàn giao thiết bị")

    authorized_user = fields.Char(string="Người được phép sử dụng")

    license_user = fields.Binary(string="Giấy phép cho người sử dụng ")

    level1_unit = fields.Many2one('ptd.unit.manager', string="Đơn vị quản lý cấp 1",required = True)
    install_location_id=fields.Many2one('ptd.install.location', string="Vị trí lắp đặt")

    ttr = fields.Text("TTR đầu tư")

    invest_project = fields.Text("Đề tài / Dự án")

    invest_value = fields.Integer("Giá trị đầu tư")

    # THÔNG TIN QUẢN LÝ CHẤT LƯỢNG

    quality_status = fields.Selection(
        string='Status*',
        selection=[('use', 'Use'),
                   ('repair', 'Repair'),
                   ('damaged', 'Damaged'),
                   ('liquidated', 'Liquidated')],
        tracking=True
    )

    broken_ids= fields.One2many(
        comodel_name='ptd.broken',
        inverse_name='broken_id',
        string='Lịch sử hỏng',
        tracking=True,
        track_visibility='onchange',
        required=False)
    quality_level = fields.Selection(
        string='Phâm cấp chất lượng',
        selection=[('1', 'Level A'),
                   ('2', 'Level AA'),
                   ('3', 'Level B'),
                   ('4', 'Level BB')],
        default='1',
        tracking=True
    )
    transfer_date = fields.Date("Ngày chuyển cấp")

    transfer_reason = fields.Char("Nguyên nhân chuyển cấp")

    maintenance_cycle = fields.Integer("Chu kỳ bảo dưỡng", require = True)

    stand_link_type = fields.Selection(
        string='Loại liên kết chuẩn',
        selection=[('1', 'Kiểm định'),
                   ('2', 'Hiệu chỉnh'),
                   ('3', 'Check technique')],
        default='1',
        tracking=True
    )
    stand_link_cycle = fields.Integer("Chu kỳ liên kết chuẩn (tháng)")

    # THÔNG TIN ĐẶC TÍNH KĨ THUẬT

    technical_characteristics_ids= fields.One2many(
        comodel_name='ptd.technical.characteristics',
        inverse_name='technical_characteristics_id',
        string='Thông tin đặc điểm kĩ thuật',
        tracking=True,
        track_visibility='onchange',
        required=False)

    # THÔNG TIN LIÊN KẾT CHUẨN

    check_or_correct_ids = fields.One2many(
        comodel_name='ptd.check.or.correct',
        inverse_name='check_or_correct_id',
        string='Check/Correct',
        tracking=True,
        track_visibility='onchange',
        required=False)

    # THÔNG TIN BẢO DƯỠNG

    maintain_info_ids = fields.One2many(
        comodel_name='ptd.maintain.info',
        inverse_name='maintain_info_id',
        string='Thông tin bảo dưỡng',
        tracking=True,
        track_visibility='onchange',
        required=False)

    @api.model
    def create(self, vals):
        print(vals['year_manufacture'])
        print(vals['year_use'])
        if vals['asset_code'].isalnum() == False:
            raise UserError("Mã QLTS: chỉ gồm ký tự chữ hoặc số")
        if vals['serial_number'].isalnum() == False:
            raise UserError("Số hiệu: chỉ gồm ký tự chữ hoặc số")
        if vals['description']!=0 and len(vals['description'])>=300:
            raise UserError(
                "Mô tả tối đa 300 ký tự")
        if vals['year_manufacture'] >= vals['year_use']:
            raise ValidationError("Năm sử dụng không hợp lệ")
        else:
            result = super(PhuongTienDo, self).create(vals)
        return result

    def write(self, vals):

        #update Mã QLTS
        if 'asset_code' in vals:
            if len(vals['asset_code'])==0:
                raise UserError("Trường: asset_number trống ")
            else:
                if vals['asset_code'].isalnum() == False:
                    raise UserError("Mã QLTS: chỉ gồm ký tự chữ hoặc số")

        #update số hiệu thiết bị
        # print(len(vals['serial_number']))
        if 'serial_number' in vals:
            if len(vals['serial_number'])==0:
                raise UserError("Trường: serial_number trống ")
            else:
                if vals['serial_number'].isalnum() == False:
                    raise UserError("Số hiệu chỉ gồm ký tự chữ hoặc số")
        # Update điều kiện năm sản xuất là năm đưa vào sử dụng
        if 'year_manufacture' in vals or 'year_use' in vals :
            date1=self.year_manufacture
            date2=self.year_use
            # print(date2)
            # print(type(date2))
            # print(type(vals['year_use']))
            if 'year_manufacture' in vals and 'year_use' in vals:
                if datetime.strptime(str(vals['year_manufacture']),"%Y-%m-%d").date() >= datetime.strptime(str(vals['year_use']),"%Y-%m-%d").date():
                    raise ValidationError("Năm sử dụng không hợp lệ")
            elif 'year_manufacture' in vals and 'year_use' not in vals:
                if datetime.strptime(str(vals['year_manufacture']),"%Y-%m-%d").date() >= datetime.strptime(str(date2),"%Y-%m-%d").date():
                    raise ValidationError("Năm sử dụng không hợp lệ")
            else:
                if datetime.strptime(str(date1),"%Y-%m-%d").date()>= datetime.strptime(str(vals['year_use']),"%Y-%m-%d").date():
                    raise ValidationError("Năm sử dụng không hợp lệ")



        # update lại ngày chuyển cấp và nguyên nhân mỗi lần thay đổi phân cấp
        if 'quality_level' in vals:
            if 'transfer_reason' not in vals or 'transfer_date' not in vals:
                raise UserError(
                   "Nhập lại đầy đủ nguyên nhân và ngày chuyển cấp")
            else:
                if vals['transfer_reason']==False:
                    raise UserError(
                        "Nhập lại nguyên nhân chuyển cấp")
                if vals['transfer_date']==False:
                    raise UserError(
                        "Nhập lại ngày chuyển cấp")
                else:
                    result = super(PhuongTienDo, self).write(vals)
        else:
            if 'transfer_reason' in vals or 'transfer_date' in vals:
                raise UserError(
                   "Không được sửa nguyên nhân và ngày thay đổi phân cấp chất lượng")
            else:
                result = super(PhuongTienDo, self).write(vals)
        return result

    def unlink(self):
        result = super(PhuongTienDo, self).unlink()
        print(result)
