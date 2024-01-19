import random

cat = []

color = ['orage', 'gray', 'black']

for i in range(100):
    cat.append(random.choice(color))
print(cat)

result = 'оранжевый кот есть' if 'orange' in cat else 'оранжевый кота нет'
print(result)
