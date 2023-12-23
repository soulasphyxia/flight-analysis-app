import openpyxl

def parse(file) -> list:
    data = []
    wb = openpyxl.load_workbook(file)
    ws = wb.active
    for i in range(2, ws.max_row + 1):
        row = [ws.cell(row = i, column = x).value for x in range(1,ws.max_column + 1)]
        row = list(map(str, row))
        row[5] = row[5].split(" ")[0]
        row[6] = row[6].split(" ")[0]
        data.append(row)
    return data
    
    