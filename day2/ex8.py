import openpyxl

from openpyxl.styles import Font, colors, PatternFill, Border, Side
from openpyxl.formatting.rule import CellIsRule

filename = 'video2old.xlsx'
wb = openpyxl.load_workbook(filename)
ws = wb.active

print(ws.title)  # vgsales

# # zmiana nazwy arkusza
# ws.title = "Video Games Sales Data"
#
# wb.save(filename)
# wb.close()

sheet_names = wb.sheetnames
print(sheet_names)
# ['Video Games Sales Data', 'Total Sales by Genre', 'Breakdown of Sales by Genre', 'Breakdown of Sales by Year']

sheet = wb[sheet_names[1]] # indek 1, arkusz numer 2
wb.active = wb.index(sheet)

ws = wb.active
print(ws.title) # Total Sales by Genre
