from odoo import models


class BaoCaoChiTietXlsx(models.AbstractModel):
    _name = 'report.mock_odoo1.baocaosoquanlydonvi_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet('Báo cáo sổ quản lý trang bị đo lường - thử nghiệm')
        bold = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#fffbed', 'border': True})
        title = workbook.add_format({
            'bold': True,
            'align': 'center',
            'font_size': 20,
            'bg_color': '#f2eee4',
            'border': True})
        merge_format = workbook.add_format({'bold': True, 'align': 'center', 'border': True})
        data_row_style = workbook.add_format({'bold': False, 'align': 'center', 'border': True})

        sheet.merge_range('A1:S1', 'BÁO CÁO SỔ QUẢN LÝ TRANG BỊ ĐO LƯỜNG - THỬ NGHIỆM', title)
        date_format = workbook.add_format({'num_format': 'dd/mm/yy','bold': False, 'align': 'center', 'border': True})

        # sheet.write(a,b,'c') : a_ row ; b_col, c_text(số thì k cần dấu ' ') (có thể tạo 1 cái)
        # sheet.merge_range(first_row, first_col, last_row, last_col, data [,merge_format]
        # sheet.set_column(first col, last_col, width [,cell_format]) (cột đầu tiên, cột cuối cùng, chiều rộng của các cột)

        sheet.merge_range('A3:A4', 'STT', merge_format)
        sheet.merge_range('B3:B4', 'Trang bị đồng bộ phụ tùng', merge_format)
        sheet.merge_range('C3:C4', 'Ký hiệu', merge_format)
        sheet.merge_range('D3:D4', 'Số hiệu', merge_format)
        sheet.merge_range('E3:E4', 'Nhóm PTĐ', merge_format)
        sheet.merge_range('F3:F4', 'Chủng loại PTĐ', merge_format)
        sheet.merge_range('G3:G4', 'Đơn vị tính', merge_format)
        sheet.merge_range('H3:H4', 'Số lượng', merge_format)
        sheet.merge_range('I3:I4', 'Nơi (hãng) SX', merge_format)
        sheet.merge_range('J3:J4', 'Năm SX', merge_format)
        sheet.merge_range('K3:K4', 'Năm SD', merge_format)
        sheet.merge_range('L3:L4', 'Đặc tính kỹ thuật đo lường', merge_format)
        sheet.merge_range('M3:M4', 'Cấp CL', merge_format)
        sheet.merge_range('N3:N4', 'Chu kỳ KĐHC', merge_format)
        sheet.merge_range('O3:O4', 'Hiệu lực KĐHC', merge_format)
        sheet.merge_range('P3:P4', 'Số GCN KĐHC', merge_format)
        sheet.merge_range('Q3:Q4', 'Đơn vị KĐHC', merge_format)
        sheet.merge_range('R3:R4', 'Cấp quản lý (TĐ hay BQP)', merge_format)
        sheet.merge_range('S3:S4', 'Ghi chú', merge_format)


        sheet.set_column('A:A', 5)
        sheet.set_column('B:B', 24)
        sheet.set_column('C:C', 10)
        sheet.set_column('D:D', 10)
        sheet.set_column('E:E', 10)
        sheet.set_column('F:F', 14)
        sheet.set_column('G:G', 11)
        sheet.set_column('H:H', 10)
        sheet.set_column('I:I', 13)
        sheet.set_column('J:J', 9)
        sheet.set_column('K:K', 9)
        sheet.set_column('L:L', 25)
        sheet.set_column('M:M', 7)
        sheet.set_column('N:N', 12)
        sheet.set_column('O:O', 14)
        sheet.set_column('P:P', 14)
        sheet.set_column('Q:Q', 14)
        sheet.set_column('R:R', 26)
        sheet.set_column('S:S', 15)


        records = self.env['ptd.ptd'].search([])

        docs = []
        i = 1

        for record in records:
            docs.append({
                'id' : i,
                'name': record.name,
                'model': record.model,
                'serial_number': record.serial_number,
                'device_group_id':record.device_group_id.name,
                'type_equip_id':record.type_equip_id.name,
                'unit_id':record.unit_id.name,
                'country_id':record.country_id.name,
                'year_manufacture':record.year_manufacture,
                'year_use' :record.year_use,
                # 'technical_properties': record.technical_properties,
                'quality_level': record.quality_level,
                'maintenance_cycle':record.maintenance_cycle,
                'level_BQP':record.level_BQP,
                'description':record.description,

                'check_or_correct_ids1':record.check_or_correct_ids.validity_date,
                'check_or_correct_ids2':record.check_or_correct_ids.certificate_number,
                'check_or_correct_ids3':record.check_or_correct_ids.organisation_id,
            })
            i += 1

        row = 4
        col = 0

        for doc in docs:

            sheet.write(row, col, doc['id'],data_row_style)
            sheet.write(row, col+1, doc['name'],data_row_style)
            sheet.write(row, col+2, doc['model'],data_row_style)
            sheet.write(row, col+3, doc['serial_number'],data_row_style)
            sheet.write(row, col+4, doc['device_group_id'],data_row_style)
            sheet.write(row, col+5, doc['type_equip_id'],data_row_style)
            sheet.write(row, col+6, doc['unit_id'],data_row_style)
            sheet.write(row, col+7, "1",data_row_style)
            sheet.write(row, col+8,doc['country_id'],data_row_style)
            sheet.write(row, col+9, doc['year_manufacture'],data_row_style)
            sheet.write(row, col+10, doc['year_use'],date_format)
            sheet.write(row, col+11, "",data_row_style)
            sheet.write(row, col+12, doc['quality_level'],data_row_style)
            sheet.write(row, col+13, doc['maintenance_cycle'],data_row_style)

            if doc['check_or_correct_ids1'] != '':
                sheet.write(row, col+14, doc['check_or_correct_ids1'],date_format)

            if doc['check_or_correct_ids2'] != '':
                sheet.write(row, col+15, doc['check_or_correct_ids2'],data_row_style)

            if doc['check_or_correct_ids3'] != '':
                sheet.write(row, col+16, doc['check_or_correct_ids3'],data_row_style)



            if doc['level_BQP'] == True:
                sheet.write(row, col+17, "BQP",data_row_style)
            else:
                sheet.write(row, col+17, "TĐ",data_row_style)

            sheet.write(row, col+18, doc['description'],data_row_style)

            row += 1

