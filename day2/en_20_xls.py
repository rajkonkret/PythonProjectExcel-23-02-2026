import xlwt

# pip install xlwt==1.3.0

# do zapisu plików xls
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Dane")

sheet.write(0, 0, "Imie")
sheet.write(0, 1, "Wiek")
sheet.write(1, 0, "Jan")
sheet.write(1, 1, 28)

workbook.save('plik_xlwt.xls')
