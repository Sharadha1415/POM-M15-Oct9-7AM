import xlrd

def read_excel_data(path, sheetname):
    workbook = xlrd.open_workbook(path)             ## book obj
    worksheet = workbook.sheet_by_name(sheetname)       ## sheet obj
    rows = worksheet.get_rows()                     ## generator obj
    header = next(rows)

    data_ = {}
    for ele in rows:
        data_[ele[0].value] = ele[1].value

    return data_

path = r'C:\Users\Ramya\PycharmProjects\POM-M15-Oct9-7AM\external_files\data.xlsx'
print(read_excel_data(path, 'reg'))





























