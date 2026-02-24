import pandas as pd

data = [
    ['Adiya', 179],
    ['Samen', 189],
    ['Darek', 169],
    ['John', 199],
]

column_names = ['Name', "Height"]

df = pd.DataFrame(data, columns=column_names)

writer = pd.ExcelWriter("excel_with_list.xlsx", engine="xlsxwriter")

# df.to_excel(writer)
# df.to_excel(writer, index=False)
df.to_excel(writer, index=False, sheet_name='first_sheet', startrow=3, startcol=3)
writer.close()
