from csv import DictReader

with open('inflation_russia.csv', encoding='utf-8') as f:
    dr = DictReader(f, delimiter=';')
    print(dr.fieldnames)
    for row in dr:
        print(row)