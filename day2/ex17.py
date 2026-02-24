import pandas as pd

df = pd.read_excel("excel_with_multiple_sheets.xlsx", sheet_name=2)
print("The dataframe is:")
print(df)
# The dataframe is:
#      Name  Marks
# 0  Addiya    179
# 1   Samen    189
# 2   Darek    199
# 3    John    169

df = pd.read_excel("excel_with_multiple_sheets.xlsx", sheet_name='marks')
print("The dataframe is:")
print(df)
# The dataframe is:
#      Name  Marks
# 0  Addiya    179
# 1   Samen    189
# 2   Darek    199
# 3    John    169

dane = pd.ExcelFile("excel_with_multiple_sheets.xlsx")
print(dane.sheet_names)  # ['height', 'weight', 'marks']

# wczytanie konkretnej kolumny
df = pd.read_excel('excel_with_multiple_sheets.xlsx', sheet_name="marks", usecols=['Name'])
print(df)
#      Name
# 0  Addiya
# 1   Samen
# 2   Darek
# 3    John
