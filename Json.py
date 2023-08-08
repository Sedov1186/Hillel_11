import json

student_data = {
    123456: {'Age': 37},
    147852: {'name': 'Dmytro'},
    258741: {'A country': 'Ukraine'},
    369852: {'Kyiv': None},  # Уточните, что здесь ожидается
    369147: {'Year of birth': 1986},
}

with open('task_01.json', 'w') as f:
    json.dump(student_data, f, indent=4, ensure_ascii=False)