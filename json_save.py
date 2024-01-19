import json

person = {
    'name': 'Alex',
    'age': 14,
    'phones': ['8958', '5584341']
}
a = [6, 58, 94 ]

result = json.dumps(person)
d = json.dumps(a)
print(result)
print(type(result))
print(d)
print(type(d))
