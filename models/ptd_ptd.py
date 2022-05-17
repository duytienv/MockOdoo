from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta
class PhuongTienDo(models.Model):
    _name = "ptd.ptd"
    _description = "Create measuring device"


    # THÔNG TIN CHUNG


    asset_code = fields.Char("Mã QLTS")
    name = fields.Char("Tên thiết bị")

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



    year_use = fields.Date(string="Năm đưa vào sử dụng")
    # year_test = fields.Date(string="Năm TEST")
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
        string='Kiểm định/ Hiệu chỉnh',
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

    def year_selection(self):
        year = 2000
        year_list = []
        while year != 2030:
            year_list.append((str(year), str(year)))
            year += 1
        return year_list

    year_manufacture = fields.Selection(
        year_selection,
        string="Năm sản xuất",
        default="",  # as a default value it would be 2019
    )
    #
    # @api.depends('year_use')
    # def _test(self):
    #     if self.year_use:
    #         self.year_test = datetime.strptime(str(self.year_use), "%Y-%m-%d").date() + timedelta(days=10)

    @api.onchange('maintain_info_ids')
    def _onchange_maintain_info_ids(self):
        print(self._origin.maintain_info_ids)
        print(self.maintain_info_ids)
        len_origin = len(self._origin.maintain_info_ids)
        if len_origin > 0:
            if len_origin < len(self.maintain_info_ids):
                if self.maintain_info_ids[len_origin].implementation_date < self._origin.maintain_info_ids[len_origin - 1].implementation_date:
                    raise UserError('Ngày hỏng không hợp lệ')
            if len_origin == len(self.maintain_info_ids):
                print(self.maintain_info_ids[0].implementation_date)
                print(self._origin.maintain_info_ids[len_origin - 2].implementation_date)
                if self.maintain_info_ids[0].implementation_date < self._origin.maintain_info_ids[len_origin - 2].implementation_date:
                    raise UserError('Ngày hỏng không hợp lệ')


    @api.onchange('broken_ids')
    def _onchange_broken_ids(self):
        print(self._origin.broken_ids)
        print(self.broken_ids)
        len_origin=len(self._origin.broken_ids)
        if len_origin>0:
            if len_origin<len(self.broken_ids):
                if self.broken_ids[len_origin].fail_time < self._origin.broken_ids[len_origin -1].fail_time:
                    raise UserError('Ngày hỏng không hợp lệ')
            if len_origin == len(self.broken_ids):
                print(self.broken_ids[0].fail_time)
                print(self._origin.broken_ids[len_origin - 2].fail_time)
                if self.broken_ids[0].fail_time < self._origin.broken_ids[len_origin -2].fail_time:
                    raise UserError('Ngày hỏng không hợp lệ')


    #thời gian giữa 2 lần kiểm định/HC
    @api.onchange('check_or_correct_ids')
    def _onchange_check_or_correct_ids(self):
        # print(self._origin.check_or_correct_ids)
        # print(self.check_or_correct_ids)
        len_origin = len(self._origin.check_or_correct_ids)
        if len_origin > 0:
            if len_origin < len(self.check_or_correct_ids):
                # print(self.check_or_correct_ids[len_origin].implementation_date)
                # print(self._origin.check_or_correct_ids[len_origin - 1].implementation_date)
                if self.check_or_correct_ids[len_origin].implementation_date < self._origin.check_or_correct_ids[len_origin - 1].implementation_date:
                    raise UserError('Ngày thực hiện không hợp lệ')
                if self.check_or_correct_ids[len_origin].validity_date < self._origin.check_or_correct_ids[len_origin - 1].validity_date:
                    raise UserError('Ngày hiệu lực không hợp lệ')
            if len_origin == len(self.check_or_correct_ids):
                # print(self.check_or_correct_ids[0].implementation_date)
                # print(self._origin.check_or_correct_ids[len_origin - 2].implementation_date)
                if self.check_or_correct_ids[0].implementation_date < self._origin.check_or_correct_ids[len_origin - 2].implementation_date:
                    raise UserError('Ngày thực hiện không hợp lệ')
                if self.check_or_correct_ids[0].validity_date < self._origin.check_or_correct_ids[len_origin - 2].validity_date:
                    raise UserError('Ngày hiệu lực không hợp lệ')





    @api.model
    def create(self, vals):
        if vals['asset_code'].isalnum() == False:
            raise UserError("Mã QLTS: chỉ gồm ký tự chữ hoặc số")
        if vals['serial_number'].isalnum() == False:
            raise UserError("Số hiệu: chỉ gồm ký tự chữ hoặc số")
        if vals['description']!=0 and len(vals['description'])>=300:
            raise UserError(
                "Mô tả tối đa 300 ký tự")
        if int(vals['year_manufacture']) > int(str(vals['year_use'][:4])):
            raise ValidationError("Năm đưa vào sử dụng không hợp lệ")
        else:
            result = super(PhuongTienDo, self).create(vals)
        return result

    def write(self, vals):
        # update Mã QLTS
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
            date1 = self.year_manufacture
            date2 = str(self.year_use)
            if 'year_manufacture' in vals:
                date1=int(vals['year_manufacture'])
                # print(date1)
            if 'year_use' in vals:
                date2 =vals['year_use']
            if int(date2[:4]) < int(date1):
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

    # @api.onchange('year_use')
    def display(self):
        self.year_test=self.year_use + timedelta(days=10)
        print(self.year_test)
        # print(type(self.year_use + timedelta(days=10)))



