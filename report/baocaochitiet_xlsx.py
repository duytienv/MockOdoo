from odoo import models

class BaoCaoChiTietXlsx(models.AbstractModel):
    _name = 'report.mock_odoo1.baocaochitiet_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet('Báo cáo chi tiết')
        bold = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#fffbed', 'border': True})
        title = workbook.add_format(
            {'bold': True, 'align': 'center', 'font_size': 20, 'bg_color': '#f2eee4', 'border': True})
        merge_format = workbook.add_format({'bold': True, 'align': 'center', 'border': True})

        sheet.merge_range('A1:Y1', 'BÁO CÁO CHI TIẾT VỀ PHƯƠNG TIỆN ĐO LƯỜNG TRONG TOÀN TẬP ĐOÀN', title)
        date_format = workbook.add_format({'num_format': 'dd/mm/yy'})
        cell_format = workbook.add_format({'bold': True})


        # sheet.write(a,b,'c') : a_ row ; b_col, c_text(số thì k cần dấu ' ') (có thể tạo 1 cái)
        # sheet.merge_range(first_row, first_col, last_row, last_col, data [,merge_format]
        # sheet.set_column(first col, last_col, width [,cell_format]) (cột đầu tiên, cột cuối cùng, chiều rộng của các cột)


        sheet.merge_range('A3:A5', 'STT', merge_format)
        sheet.merge_range('B3:B5', 'Tên phương tiện đo', merge_format)
        sheet.merge_range('C3:C5', 'Mã hàng hóa', merge_format)
        sheet.merge_range('D3:D5', 'Part Number', merge_format)
        sheet.merge_range('E3:E5', 'Serial', merge_format)
        sheet.merge_range('F3:F5', 'Tình trạng', merge_format)
        sheet.merge_range('G3:G5', 'Thời gian đưa vào sử dụng', merge_format)

        sheet.merge_range('H3:J3', 'Thông tin quản lý', merge_format)
        sheet.merge_range('K3:N3', 'Phân cấp chất lượng', merge_format)
        sheet.merge_range('O3:U3', 'Công tác kiểm định / Hiệu chuẩn (KĐHC)', merge_format)

        sheet.write('V3', 'Công tác bảo trì, bảo dưỡng', merge_format)
        sheet.merge_range('W3:X3', 'Công tác bảo hành sửa chữa', merge_format)
        sheet.merge_range('Y3:Y5', 'Ghi chú', merge_format)

        # Trong thông tin quản lý
        sheet.merge_range('H4:H5', 'Mã nhân viên', merge_format)
        sheet.merge_range('I4:I5', 'Họ và tên', merge_format)
        sheet.merge_range('J4:J5', 'Đơn vị quản lý', merge_format)

        # Trong phân cấp chất lượng
        sheet.merge_range('K4:K5', 'Cấp 1', merge_format)
        sheet.merge_range('L4:L5', 'Cấp 2', merge_format)
        sheet.merge_range('M4:M5', 'Cấp 3', merge_format)
        sheet.merge_range('N4:N5', 'Cấp 4', merge_format)

        # Trong công tác kiểm định / hiệu chuẩn (KĐHC)
        sheet.merge_range('O4:O5', 'Chu kỳ kiểm định, hiệu chuẩn', merge_format)
        sheet.merge_range('P4:P5', 'Thời gian thực hiện KĐ/HC', merge_format)
        sheet.merge_range('Q4:Q5', 'Đối tác thực hiện KĐHC', merge_format)
        sheet.merge_range('R4:R5', 'Ghi rõ KĐ hay HC', merge_format)
        sheet.merge_range('S4:U4', 'Kết quả kiểm định / hiệu chuẩn', merge_format)
        sheet.write('S5', 'Đạt', merge_format)
        sheet.write('T5', 'Không đạt', merge_format)
        sheet.write('U5', 'Nguyên nhân không đạt', merge_format)

        # Trong công tác bảo trì bảo dưỡng
        sheet.merge_range('V4:V5', 'Thời gian thực hiện gần nhất', merge_format)

        #Trong công tác bảo hành sửa chữa
        sheet.merge_range('W4:W5', 'Thời gian hỏng gần nhất', merge_format)
        sheet.merge_range('X4:X5', 'Nguyên nhân hỏng', merge_format)

        sheet.set_column('A:A',5)
        sheet.set_column('B:B',18)
        sheet.set_column('C:C',12)
        sheet.set_column('D:D',11)
        sheet.set_column('E:E',10)
        sheet.set_column('F:F',10)
        sheet.set_column('G:G',25)

        sheet.set_column('H:J',50)
        sheet.set_column('H:H',15)
        sheet.set_column('I:I',15)
        sheet.set_column('J:J',20)

        sheet.set_column('K:N',20)
        sheet.set_column('K:K',5)
        sheet.set_column('L:L',5)
        sheet.set_column('M:M',5)
        sheet.set_column('N:N',5)

        sheet.set_column('O:O',27)
        sheet.set_column('P:P',25)
        sheet.set_column('Q:Q',21)
        sheet.set_column('R:R',17)
        #Công tác kiểm định / hiệu chuẩn (KĐHC)
        sheet.set_column('S:S',9)
        sheet.set_column('T:T',9)
        sheet.set_column('U:U',21)
        # Công tác bảo trì
        sheet.set_column('V:V',26)

        # Công tác sửa chữa
        sheet.set_column('W:W',22)
        sheet.set_column('X:X',18)
        # Ghi chú
        sheet.set_column('Y:Y',18)


        # records = self.env['ptd.ptd']
        #
        # docs = []
        # i = 1
        #
        # for record in records:
        #     docs.append({
        #         'id' : i,
        #         'name': record.name,
        #         'commodity_code': record.commodity_code,
        #         'serial_number': record.serial_number,
        #         # 'quality_status':record.quality_status,
        #         # 'manager_id1':record.manager_id.employee_code,
        #         # 'manager_id2':record.manager_id.name,
        #         # 'unit_manager_id':record.unit_manager_id.name,
        #         # # Cấp phải so sánh
        #         # 'quality_level':record.quality_level,
        #         #
        #         # 'maintenance_cycle':record.maintenance_cycle,
        #         # # KĐ/HC
        #
        #     })
        #     i += 1
        #
        # row = 7
        # col = 0
        #
        # for doc in docs:
        #     # Id
        #     sheet.write(row, col, doc['id'])
        #     # Tên thiết bị
        #     sheet.write(row, col + 1, doc['name'])
        #     # # Mã hàng hóa
        #     sheet.write(row, col + 2, doc['commodity_code'])
        #     # # Part number
        #     # sheet.write(row,col+3, doc[''])
        #     # # Serial
        #     sheet.write(row, col + 4, doc['serial_number'])
        #     # # Trạng thái
        #     # sheet.write(row,col+5, doc['quality_status'], date_format)
        #     # # Thời gian đưa vào sử dụng
        #     # sheet.write(row,col+6, doc[''])
        #     # # Mã nhân viên
        #     # sheet.write(row,col+7, doc['manager_id1'])
        #     # # Họ và tên - Chưa làm
        #     # sheet.write(row,col+8, doc['manager_id2'])
        #     # # Đơn vị quản lý - Chưa làm
        #     # sheet.write(row,col+9, doc['unit_manager_id'])
        #     # # Cấp 1
        #     # sheet.write(row,col+10, doc['quality_level'])
        #     # # Cấp 2
        #     # sheet.write(row,col+11, doc['quality_level'])
        #     # # Cấp 3
        #     # sheet.write(row,col+12, doc['quality_level'])
        #     # # Cấp 4
        #     # sheet.write(row,col+13, doc['quality_level'])
        #     # # Chu kì kiểm định hiệu chuẩn
        #     # sheet.write(row,col+14, doc['maintenance_cycle'])
        #     # # Thời gian thực hiện KĐHC gần nhất
        #     # sheet.write(row,col+15, doc[''])
        #     # # Đối tác thực hiện KĐHC
        #     # sheet.write(row,col+16, doc[''])
        #     # # Ghi rõ KĐ hay HC
        #     # sheet.write(row,col+17, doc[''])
        #     # # Đạt
        #     # sheet.write(row,col+18, doc[''])
        #     # # Không đạt
        #     # sheet.write(row,col+19, doc[''])
        #     # # Nguyên nhân không đạt
        #     # sheet.write(row,col+20, doc[''])
        #     # # Thời gian thực hiện gần nhất
        #     # sheet.write(row,col+21, doc[''])
        #     # # Thời gian hỏng gần nhất
        #     # sheet.write(row,col+22, doc[''])
        #     # # Nguyên nhân hỏng
        #     # sheet.write(row,col+23, doc[''])
        #     # # Ghi chú
        #     # sheet.write(row,col+24, doc['description'])
        #
        #     row += 1

