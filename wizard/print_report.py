from odoo import fields, models
class PrintReport(models.TransientModel):
    _name = "ptd.print.report"
    type = fields.Selection(
        string='Loại báo cáo',
        selection=[('1', 'Báo cáo chi tiết'),
                   ('2', 'Báo cáo sai lệch'),
                   ('3', 'Báo cáo thiết bị cấp BQP'),
                   ('4','Báo cáo sổ các thiết bị TN')],
        tracking=True
    )
    name = fields.Many2many('ptd.ptd',  string="Chọn thiết bị")

    def print_report(self):
        data={
            'form':self.read()[0],
        }
        return self.env.ref('Mock_odoo.account_test1_id').report_action(self, data = data)
        # return self.env.ref('Mock_odoo.account_test1_id').report_action(self)

