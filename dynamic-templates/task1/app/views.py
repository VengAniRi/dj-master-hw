from django.shortcuts import render
from csv import DictReader


class DataRow:
    def __init__(self, datalst):
        self.year = datalst[0]
        self.vals = datalst[1:-1]
        self.total = datalst[-1]

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    with open('inflation_russia.csv', encoding='utf-8') as f:
        dr = DictReader(f, delimiter=';')
        col_names = dr.fieldnames.copy()
        rows = [DataRow(list(row.values())) for row in dr]
        # print(dr.fieldnames)
        # for row in dr:
        #     print(row)
    context = {'col_names': col_names, 'rows': rows}

    return render(request, template_name,
                  context)