# https://djbook.ru/rel1.5/howto/initial-data.html
# генератор контента в формате json для заполнения БД через django


import json
import random


n = 90  # записей
first_names = ['Никита', 'Аркадий', 'Арсений', 'Павел', 'Михаил', 'Дмитрий', 'Семен', 'Виктор', 'Алексей']
last_names = ['Серебренников', 'Иванов', 'Петров', 'Сидоров', 'Сафронов', 'Гомелев', 'Семенов', 'Куприянов', 'Кипелов', 'Морозов', 'Удальцов']
middle_names = ['Владимирович', 'Вячеславович', 'Сергеевич', 'Иванович', 'Александрович', 'Павлович']


with open('content.json', 'w', encoding='utf-8') as content:
    content.write('[')
    for i in range(0, n):
        content.write(json.dumps(
                {
                    'model': 'main_app.student',
                    'fields': {
                        'first_name': random.choice(first_names),
                        'last_name': random.choice(last_names),
                        'middle_name': random.choice(middle_names),
                        'birth_day': str(random.randint(1989, 1991)) + '-' + str(random.randint(1, 12)) + '-' + str(random.randint(1, 28)),
                        'stud_number': random.choice(['A', 'B', 'C']) + str(random.randint(10000, 99999)),
                        'group': random.choice(['0001', '0002', '0003']),
                        'is_captain': 'False'
                    }
                },
                ensure_ascii=False))
        if not i == n-1:
            content.write(',\n')
    content.write(']')