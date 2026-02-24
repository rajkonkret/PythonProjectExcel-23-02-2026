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

df.to_excel(writer)
writer.close()
