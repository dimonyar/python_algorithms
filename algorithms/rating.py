import random

randomlist = []
for i in range(0, 30):
    n = random.randint(0, 100)
    randomlist.append(n)
print(randomlist)

marks = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}

for i in randomlist:
    if 90 < i <= 100:
        marks['A'] += 1
    elif 80 < i <= 90:
        marks['B'] += 1
    elif 70 < i <= 80:
        marks['C'] += 1
    elif 60 < i <= 70:
        marks['D'] += 1
    else:
        marks['E'] += 1
print(marks)
