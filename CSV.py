#import json

#student_data = {

#123456: (37),
#147852: ('Dmytro'),
#258741: ('Ukraine'),
#369852: ('Kyiv'),
#369147: ('Year of birth', 1986),
#}
#with open('task_01.json', 'w') as f:
#    json.dump(student_data, f)
#    print(student_data)

#Прочитать сохранённый json-файл из предыдущего задания и записать данные
# на диск в csv-файл, первой строкой которого озаглавив каждый столбец
# и добавив новый столбец “телефон”. Кроме этого необходимо для
# каждой записи добавить значение новой ячейки “телефон”.
# Значение должно быть заполнено случайными цифрами.
#Названия столбцов будут следующие:
#ID, Имя, Возраст, Телефон.

#При этом значения для первых трёх ячеек необходимо достать
# из json-файла для каждой записи, а значение новой ячейки Телефон
# сформировать.


import csv
name_of_fiwlds1 = 'ID'
name_of_fiwlds2 = 'Имя'
name_of_fiwlds3 = 'Возраст'
with open('data.csv', 'w', newline=None) as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(
        [name_of_fiwlds1, name_of_fiwlds2,
         name_of_fiwlds3]

    )
users_data = [
    ['123456', 'Dmytro', '37']
]
for user in users_data:
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            user
        )


