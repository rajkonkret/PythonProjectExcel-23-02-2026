import csv

# wykrycie znaku podziału w pliku csv
# [',', '\t', ';', ' ', ':']
with open('wyniki.csv', "r") as f:
    data = csv.Sniffer().sniff(f.read(1024))
    print(data.delimiter)  # ,
    print(data.quotechar)  # "
