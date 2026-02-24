# pandas - biblioteka do przetwarzania danych
import pandas as pd

# tworzymy tabelki w pamięci
writer = pd.ExcelWriter('empty_excel.xlsx')

empty_dataframe = pd.DataFrame()  # tablica/ macierz w pandas

# zapisanie danych do pliku excel
empty_dataframe.to_excel(writer, sheet_name='empty')
writer.close()  # musimy zamykać writer
