from odoo import fields, models
from odoo.exceptions import UserError
class PrintReport(models.TransientModel):
    _name = "ptd.print.report"
    type = fields.Selection(
        string='Loại báo cáo',
        selection=[('1', 'Báo cáo chi tiết'),
                   ('2', 'Báo cáo sai lệch'),
                   ('3', 'Báo cáo thiết bị cấp BQP'),
                   ('4', 'Báo cáo sổ các thiết bị TN')],
        tracking=True
    )
    record_id = fields.Many2many('ptd.ptd',  string="Chọn thiết bị")

    def print_report_pdf(self):
        if not self.record_id:
            raise UserError('Chưa chọn thiết bị cần in')
        if not self.type:
            raise  UserError('Chọn loại báo cáo muốn in')
        if self.type=='1':
            return self.env.ref('mock_odoo1.account_test1_id').report_action(self.record_id)
        if self.type=='2':
            return self.env.ref('mock_odoo1.account_test2_id').report_action(self.record_id)
        if self.type=='3':
            return self.env.ref('mock_odoo1.account_test3_id').report_action(self.record_id)
        if self.type=='4':
            return self.env.ref('mock_odoo1.account_test4_id').report_action(self.record_id)
        # return self.env.ref('mock_odoo1.account_test1_id').report_action(self)

    def print_report_csv(self):
        if not self.record_id:
            raise UserError('Chưa chọn thiết bị cần in')
        if not self.type:
            raise  UserError('Chọn loại báo cáo muốn in')
        if self.type=='1':
            return self.env.ref('mock_odoo1.account_test1_id_xls').report_action(self.record_id)
        if self.type=='2':
            return self.env.ref('mock_odoo1.account_test2_id_xls').report_action(self.record_id)
        if self.type=='3':
            return self.env.ref('mock_odoo1.account_test3_id_xls').report_action(self.record_id)
        if self.type=='4':
            return self.env.ref('mock_odoo1.account_test4_id_xls').report_action(self.record_id)

