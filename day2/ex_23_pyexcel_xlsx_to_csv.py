# konwersja plików przy pomocy pyexcel
# pip install pyexcel-csv - nie jest potrzebne od pythona 3.13

import pyexcel as pe

pe.save_book_as(file_name="wyniki.xlsx",
                dest_file_name="wyniki.csv")
