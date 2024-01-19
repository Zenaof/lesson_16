import random

cat = []

color = ['orage', 'gray', 'black']

for i in range(100):
    cat.append(random.choice(color))
print(cat)

if 'orage' in cat:
    print('оранжевый кот есть')
else:
    print('оранжевый кота нет')
print()if 'orange' in cat ('оранжевый кот есть') else ('оранжевый кота нет')