import csv
from openpyxl import Workbook

csv_filename = 'task_02.csv'
excel_filename = 'student_data.xlsx'

data = []
with open(csv_filename, 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    headers = next(csv_reader)

    for row in csv_reader:
        data.append(row)

wb = Workbook()
ws = wb.active


for row in data:
    ws.append([row[0], row[1], row[3]])

wb.save(excel_filename)