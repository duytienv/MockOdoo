from odoo import models, fields, api


class PtdSTechnicalCharacteristics(models.Model):
    _name = "ptd.technical.characteristics"
    _description = "Thông tin đặc điểm kĩ thuật"

    id = fields.Char("ID")

    parameters = fields.Char(string="Tham số")
    val_maintain = fields.Char(string="Giá trị")
    display_resolution = fields.Char(string="Phân giải hiển thị")
    exact_level = fields.Char(string="Cấp chính xác (sai số)")
    technical_characteristics_id= fields.Many2one('ptd.ptd')