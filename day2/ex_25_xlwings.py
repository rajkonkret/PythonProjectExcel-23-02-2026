import xlwings as xw
import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.random.randn(100, 5),
                  columns=[f"Próba {i}" for i in range(1, 6)])

print(df)

print(45 * "-")
print(df.head())  # pięc pierwszych wierszy
print(df.tail())
#      Próba 1   Próba 2   Próba 3   Próba 4   Próba 5
# 95 -0.103523 -0.363480 -1.404387 -1.199620  0.553087
# 96  0.756218  0.542985  0.356795  0.091866  1.757058
# 97  2.492006  1.659289  1.305899 -0.586535  1.058832
# 98 -0.727546  1.110544  0.061281 -0.609152  0.236598
# 99 -0.540616  0.048673  0.651968 -0.377953  1.212404

# xw.view(df)

book = xw.Book()
print(book.name)
print(book.sheets)

# Zeszyt2
# Sheets([<Sheet [Zeszyt2]Arkusz1>])

sheet1 = book.sheets[0]
print(sheet1.range('A1'))  # <Range [Zeszyt1]Arkusz1!$A$1>

sheet1.range('A1').value = [[1, 2],
                            [3, 4]]

sheet1.range('A4').value = "Witaj!"

print(sheet1['A1'].value)  # 1.0

print(sheet1["A1:B2"].value)  # [[1.0, 2.0], [3.0, 4.0]]
