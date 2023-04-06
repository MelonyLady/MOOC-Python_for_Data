import csv


with open("sales_dataset.csv", "r") as data_file:
    spreadsheet = csv.DictReader(data_file)
    for row in spreadsheet:
        print(row)
