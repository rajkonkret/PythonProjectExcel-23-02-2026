import pandas as pd

df = pd.DataFrame({
    "Imie": ['Anna', "Tomek", "Jan", "Jakub", "Klaudia", "Anna", "Tomek"],
    "Miasto": ["Kraków", "Warszawa", "Gdańsk", "Warszawa", "Ząbki", "Gdańsk", "Warszawa"],
    "Wynik": [88, 95, 70, 91, 60, 89, 95]
})

df_sorted = df.sort_values(by="Imie")
print(df_sorted.head)
# <bound method NDFrame.head of       Imie    Miasto  Wynik
# 0     Anna    Kraków     88
# 3    Jakub  Warszawa     91
# 2      Jan    Gdańsk     70
# 4  Klaudia     Ząbki     60
# 1    Tomek  Warszawa     95>

print("Malejąco")
# malejąco
df_sorted_desc = df.sort_values(by="Imie", ascending=False)
print(df_sorted_desc)
#       Imie    Miasto  Wynik
# 1    Tomek  Warszawa     95
# 4  Klaudia     Ząbki     60
# 2      Jan    Gdańsk     70
# 3    Jakub  Warszawa     91
# 0     Anna    Kraków     88

print("Rosnąco")
df_sorted_multi = df.sort_values(by=['Miasto', "Wynik"], ascending=[True, False])
print(df_sorted_multi)
#       Imie    Miasto  Wynik
# 2      Jan    Gdańsk     70
# 0     Anna    Kraków     88
# 1    Tomek  Warszawa     95
# 3    Jakub  Warszawa     91
# 4  Klaudia     Ząbki     60

print("Po średniej")
df_grouped_mean = df.groupby("Imie", as_index=False)["Wynik"].mean()
print(df_grouped_mean)
#       Imie  Wynik
# 0     Anna   88.0
# 1    Jakub   91.0
# 2      Jan   70.0
# 3  Klaudia   60.0
# 4    Tomek   95.0

print("po sumie")
df_grouped_sum = df.groupby("Imie", as_index=False)["Wynik"].sum()
print(df_grouped_sum)
#       Imie  Wynik
# 0     Anna     88
# 1    Jakub     91
# 2      Jan     70
# 3  Klaudia     60
# 4    Tomek     95

print("Ilość wpisów")
df_grouped_count = df.groupby("Imie").size().reset_index(name="Ilość wpisów")
print(df_grouped_count)

with pd.ExcelWriter('raport.xlsx', engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Oryginalne", index=False)
    df_sorted.to_excel(writer, sheet_name="Posortowane", index=False)
    df_grouped_mean.to_excel(writer, sheet_name="Średnia", index=False)
