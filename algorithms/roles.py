roles = {
    'admin': ['Andrews', 'Bishop', 'MacDonald', 'Taylor', 'Harrison'],
    'maintainer': ['Holmes', 'James', 'Kennedy', 'Pit', 'Benson'],
    'manager': ['Oswald', 'Daniels', 'Farrell', 'Philips', 'Russel'],
    'developer': ['Gilbert', 'Smith', 'Simpson', 'Finch', 'Hancock']
}

name = input('Please enter your name: ')

flag = False

for role in roles.keys():
    for login in roles[role]:
        if login == name:
            print('Hello', role)
            flag = True
            break
    if flag:
        break
else:
    print('Hello, Guest')
