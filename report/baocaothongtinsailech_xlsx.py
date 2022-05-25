from odoo import models

class BaoCaoChiTietXlsx(models.AbstractModel):
    _name = 'report.mock_odoo1.baocaothongtinsailech_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet('Báo cáo thông tin sai lệch')
        bold = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#fffbed', 'border': True})
        title = workbook.add_format(
            {'bold': True, 'align': 'center', 'font_size': 20, 'bg_color': '#f2eee4', 'border': True})
        merge_format = workbook.add_format({'bold': True, 'align': 'center', 'border': True})
        data_row_style = workbook.add_format({'bold': True, 'align': 'center', 'border': True})

        sheet.merge_range('A1:G1', 'BÁO CÁO THÔNG TIN SAI LỆCH', title)
        date_format = workbook.add_format({'num_format': 'dd/mm/yy'})
        cell_format = workbook.add_format({'bold': True})


        # sheet.write(a,b,'c') : a_ row ; b_col, c_text(số thì k cần dấu ' ') (có thể tạo 1 cái)
        # sheet.merge_range(first_row, first_col, last_row, last_col, data [,merge_format]
        # sheet.set_column(first col, last_col, width [,cell_format]) (cột đầu tiên, cột cuối cùng, chiều rộng của các cột)


        sheet.merge_range('A3:A4', 'STT', merge_format)
        sheet.merge_range('B3:B4', 'Tên thiết bị', merge_format)
        sheet.merge_range('C3:C4', 'Mã thiết bị', merge_format)
        sheet.merge_range('D3:F3', 'Thông tin sai lệch', merge_format)
        sheet.merge_range('G3:G4', 'Ghi chú ', merge_format)

        sheet.write('D4', 'Trường dữ liệu', merge_format)
        sheet.write('E4', 'Thông tin cũ', merge_format)
        sheet.write('F4', 'Thông tin mới', merge_format)


        sheet.set_column('A:A',8)
        sheet.set_column('B:B',25)
        sheet.set_column('C:C',25)
        sheet.set_column('D:D',30)
        sheet.set_column('E:E',30)
        sheet.set_column('F:F',30)
        sheet.set_column('G:G',25)

        records = self.env['ptd.ptd'].search([])

        docs = []
        i = 1

        for record in records:
            docs.append({
                'id' : i,
                'name': record.name,
                'commodity_code': record.commodity_code,
                'serial_number': record.serial_number,
                'country_id': record.country_id.name,
                'manufactor_id' :record.manufactor_id.name,
                'description' : record.description
            })
            i += 1

        row = 4
        col = 0

        for doc in docs:
            # Id
            sheet.write(row, col, doc['id'],data_row_style)
            sheet.write(row+1, col, "",data_row_style)

            # Tên thiết bị
            sheet.write(row, col+1, doc['name'], data_row_style)
            sheet.write(row+1, col+1, doc['name'], data_row_style)

            sheet.write(row, col+2, doc['commodity_code'],data_row_style)
            sheet.write(row+1, col+2, doc['commodity_code'],data_row_style)

            sheet.write(row, col+3, "Nước sản xuất",data_row_style)
            sheet.write(row+1, col+3, "Nhà sản xuất",data_row_style)

            sheet.write(row, col+4, doc['country_id'],data_row_style)
            sheet.write(row, col+5, doc['country_id'],data_row_style)


            sheet.write(row+1, col+4, doc['manufactor_id'],data_row_style)
            sheet.write(row+1, col+5, doc['manufactor_id'],data_row_style)

            sheet.write(row, col+6, doc['description'],data_row_style)
            sheet.write(row+1, col+6, doc['description'],data_row_style)

            row += 2
