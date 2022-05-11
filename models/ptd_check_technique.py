from odoo import models, fields, api
class PtdDeviceGroup(models.Model):
    _name = "ptd.check.technique"
    _description = "Kiểm tra kỹ thuật đo lường"

    result= fields.Selection(
        string='Kết quả',
        selection=[('1', 'Pass'), ('2', 'Fail')],
        tracking=True
    )
    implementation_date=fields.Date("Ngày thực hiện")
    performer= fields.Char("Người thực hiện")
    relative_error = fields.Char("Sai số tương đối")
    note = fields.Text(string = 'Note')