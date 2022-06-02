"""
Having two standards for a keypad layout is inconvenient!
Computer keypad's layout:
            7 8 9
            4 5 6
            1 2 3
              0

Cell phone keypad's layout:
            1 2 3
            4 5 6 
            7 8 9  
              0

Solve the horror of unstandartized keypads by providing a function that converts computer input to a number as if it was typed by a phone.

            Example:
            "789" -> "123"

Notes:
You get a string with numbers only"""

computer_to_phone = lambda numbers: numbers.translate(str.maketrans('123789', '789123'))


def test_computer_to_phone():
    assert computer_to_phone("0789456123") == "0123456789"
    assert computer_to_phone("000") == "000"
    assert computer_to_phone("94561") == "34567"
    return print('All tests from computer_to_phone passed successfully')
