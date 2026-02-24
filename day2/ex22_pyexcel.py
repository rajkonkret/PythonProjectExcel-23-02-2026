import pyexcel

# pip install pyexcel pyexcel-xlsx

data = [
    ['Imię', "Wiek"],
    ['Tomek', "38"],
    ['Kasia', "34"],
]

sheet = pyexcel.Sheet(data)
sheet.save_as("wyniki.xlsx")

# wczytanie
sheet = pyexcel.get_sheet(file_name='wyniki.xlsx')
print(sheet)
# pyexcel sheet:
# +-------+------+
# | Imię  | Wiek |
# +-------+------+
# | Tomek | 38   |
# +-------+------+
# | Kasia | 34   |
# +-------+------+
print(sheet.columns())  # <generator object Matrix.columns at 0x000001C392D92A40>

for i in sheet.columns():
    print(i)
# ['Imię', 'Tomek', 'Kasia']
# ['Wiek', '38', '34']
