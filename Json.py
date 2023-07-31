import json

student_data = {

123456: ('age', 37),
147852: ('firstName','Sedov'),
258741: ('A country', 'Ukraine'),
369852: ('Kyiv'),
369147: ('Year of birth', 1986),
}
with open('task_01.json', 'w') as f:
    json.dump(student_data, f)
    print(student_data)