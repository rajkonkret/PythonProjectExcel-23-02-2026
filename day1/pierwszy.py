import sys
from time import sleep

print()  # wypisz/wydrukuj

print()
print()
print()
print()
print("Radek")  # Radek
print('Radek')

# print('Radek")
#   File "C:\Users\Szkolenie\PycharmProjects\PythonProjectExcel-23-02-2026\day1\pierwszy.py", line 10
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 10)
#
# Process finished with exit code 1
print("Dalsza część programu")

print(type('radek'))  # <class 'str'> - dane tekstowe

print(45)
print(type(45))  # <class 'int'>, liczby całkowite

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

print("34" + "19")  # 3419, konkatenacja, łączenie stringów

print(34 + 19)  # 53

# print("34" + 19)  # TypeError: can only concatenate str (not "int") to str

print(34 * "168")
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168

print(34 * 168)  # 5712

print(25 * "-")

# liczby zmiennoprzecinkowe
print(4.56)
print(type(4.56))  # <class 'float'>

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024,
# max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15,
# mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(0.1 + 0.2)
# 0.30000000000000004
print(0.1 + 0.9)  # 1.0
#  For example, in a floating-point arithmetic with five base-ten digits,
#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal - pozwala ominąć problem zaokroglenia

# zmienna - pudełko na dane
# typowanie dynamiczne
name = "Radek"
print(name)  # Radek
print(type(name))  # <class 'str'>

name = 90
print(name)
print(type(name))

# rzutowanie typów
a = "1"
b = 0
# print(a + b)
print(int(a) + b)  # 1, int() - rzutowanie na liczbę
print(int(a) + int(b))  # 1

print(str(1) + str(1))  # str() - rzutowanie na string

print(type(1 + 2))  # <class 'int'>

tekst = "Witaj Świecie"

# teksty są niemutowalne
tekst.upper()
print(tekst)
""" Return a copy of the string converted to uppercase. """
print(tekst.upper())  # WITAJ ŚWIECIE

nowy_tekst = tekst.upper()
print(nowy_tekst)  # WITAJ ŚWIECIE

zmienna1 = "GROSS"
zmienna2 = "groß"

print(zmienna1.lower() == zmienna2.lower())  # == porównanie, False
print(zmienna1.casefold() == zmienna2.casefold())  # True

# typ logiczny True, False
print(1 != 0)  # rózne

name = "Radek"
# f - string
print(f"Nazywam się: {name}")  # Nazywam się: Radek

a = 4.5678
print(f"Liczba: {a}")  # Liczba: 4.5678
print(f"Liczba: {a:.2f}")  # Liczba: 4.57

print("Liczba:", a)  # Liczba: 4.5678

# sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.

print("Liczba:", a, sep=" <> ")  # Liczba: <> 4.5678

# %f - float
print("Liczba: %f" % a)  # Liczba: 4.567800
print("Liczba: %.2f" % a)  # Liczba: 4.57

# print("Liczba: %f" % "Radek")  # TypeError: must be real number, not str

print("""
Tekst
    wielolinijkowy""")

# "Tekst
#     wielolinijkowy"

"""Komentarz
    wielolinijkowy - dokumentacja"""

print(print.__doc__)

print(100 / 3)  # 33.333333333333336
print(100 // 3)  # 33 część calkowita z dzielenia
print(100 % 3)  # modulo, reszta z dzielenia
print(10 % 3)  # 1

zysk = 890123456543123
print(f'Nasza duza liczba: {zysk:,}')  # Nasza duza liczba: 890,123,456,543,123
print(f'Nasza duza liczba: {zysk:_}')  # Nasza duza liczba: 890,123,456,543,123
print(f'Nasza duza liczba: {zysk:_}'.replace("_", " "))
# Nasza duza liczba: 890 123 456 543 123

liczba = 1_000_000_000_000_000
print(type(liczba))
print(liczba)  # <class 'int'>, 1000000000000000

# kolekcje

# lista - przechowuje eleemnty z zachowaniem kolejności
lista = [1, 2, 3, 4, 5, 6, "Radek"]
print(type(lista))  # <class 'list'>
print(lista)  # [1, 2, 3, 4, 5, 6, 'Radek']

lista = []  # tworzenie pustej listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Klaudia")
lista.append("Jakub")
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Klaudia', 'Jakub']

# usunięcie
lista.remove("Radek")
print(lista)  # ['Tomek', 'Zenek', 'Klaudia', 'Jakub']

lista_copy = lista.copy()  # kopia danych
lista_k = lista
print(lista_k)  # ['Tomek', 'Zenek', 'Klaudia', 'Jakub']
print(lista)  # ['Tomek', 'Zenek', 'Klaudia', 'Jakub']

lista.clear()  # usunięcie wszystkich elementow z listy
print(lista_copy)  # ['Tomek', 'Zenek', 'Klaudia', 'Jakub']
print(lista)  # []
print(lista_k)  # []

# sprawdzenie adresu dla elementu
print(id(lista_copy))  # 2605498290112

# krotka (tuple) - kolekcja niemutowalna, do odczytu
# pozwala lepiej zarządzać pamiecią

krotka = tuple(lista_copy)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # ('Tomek', 'Zenek', 'Klaudia', 'Jakub')

tupla1 = "Radek", "Tomek"
# tupla1[1] = 190  # TypeError: 'tuple' object does not support item assignment

# zbiór - set
# przechowuje unikalne wartości, nie zachowuje kolejnosci
lista = [2, 5, 6, 8, 6, 7, 8, 5, 9]
zbior = set(lista)
print(zbior)  # {2, 5, 6, 7, 8, 9}

pusty_zbior = set()  # tylko i wyłącznie słowko set
pusty_zbior.add(15)
print(pusty_zbior)  # {15}

# słownik -> klucz - wartosc
slownik = {'name': 'Radek', 'age': 56}
print(slownik)  # {'name': 'Radek', 'age': 56}
print(type(slownik))  # <class 'dict'>

print(slownik.keys())  # dict_keys(['name', 'age'])
print(slownik.values())  # dict_values(['Radek', 56])
print(slownik.items())  # dict_items([('name', 'Radek'), ('age', 56)])

print(slownik['name'])  # Radek
print(slownik.get('age'))  # 56

pusty_slownik = {}
print(pusty_slownik)  # {}
print(type(pusty_slownik))  # <class 'dict'>

p_s = dict()
print(p_s)  # {}

# input() - wczytanie danych o użytkownika

# tekst = input("Podaj imię:")  # str
# print(tekst)
# print(type(tekst))

# a = input("Podaj pierwszą liczbę:")
# b = input("Podaj drugą liczbę:")
# print(int(a) + float(b))
# Podaj pierwszą liczbę:1
# Podaj drugą liczbę:2
# 3.0

print(pusty_slownik)  # {}
pusty_slownik['name'] = "Radek"
print(pusty_slownik)  # {'name': 'Radek'}

pusty_slownik.update({"age": 67})
print(pusty_slownik)

p_s.update([('name', 'Radek'), ('age', 56)])
print(p_s)  # {'name': 'Radek', 'age': 56}
