import json
import csv
import random

json_filename = 'task_01.json'
csv_filename = 'task_02.csv'

with open(json_filename, 'r') as json_file:
    student_data = json.load(json_file)

with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)

    csv_writer.writerow(['ID', 'Имя', 'Возраст', 'Телефон'])

    for id, data in student_data.items():
        name = data.get('name', '')
        age = data.get('Age', '')
        phone = ''.join([str(random.randint(0, 9)) for _ in range(10)])  # Случайный телефон
        csv_writer.writerow([id, name, age, phone])
