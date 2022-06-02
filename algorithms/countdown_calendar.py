
'''
Write a program that does:
1. Reads events from file events.txt
Each event is on a new line and formatted as next: "New Year,31.12.21"
2. For every event calculates number of days until the event and outputs:
"It is 86 days until New Year"
'''

from datetime import date, datetime


def read_data():
    with open(path) as events:
        lst = [line.replace('\n', '').split(',') for line in events]

    for i in lst:
        i[1] = datetime.strptime(i[1], '%d.%m.%y').date()
    return lst


def delta_data(x):
    return str(x - date.today()).replace(', 0:00:00', ' ')


def output():
    s = ''
    for i in read_data():
        days = delta_data(i[1])
        event = i[0]
        s += 'It is ' + days + 'until ' + event + '\n'
    return s


path = 'events.txt'


def test_output():
    assert output() == 'It is 212 days until New Year\nIt is 214 days until Birthday\n'
    return print('All tests from countdown_calendar.py passed successfully')
