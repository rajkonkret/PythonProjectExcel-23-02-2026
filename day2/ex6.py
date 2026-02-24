import openpyxl
# https://fiszki-go.cytr.us/

filename = 'video2.xlsx'

# wb = openpyxl.load_workbook('video2.xlsx')
wb = openpyxl.load_workbook(filename)
ws = wb['vgsales']

ws['P1'] = "Averages Sales"
ws['P2'] = '=AVERAGE(K2:K16328)'

wb.save(filename)
wb.close()
