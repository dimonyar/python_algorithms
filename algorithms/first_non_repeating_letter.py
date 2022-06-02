# Write a function named first_non_repeating_letter that takes a string input,
# and returns the first character that is not repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't',
# since the letter t only occurs once in the string, and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered the same
# character, but the function should return the correct case for the initial letter.
# For example, the input 'sTreSS' should return 'T'.

# If a string contains all repeating characters, it should return an empty string ("")
# or None -- see sample tests.


def first_non_repeating_letter(string):
    for i in string:
        part = string.partition(i)[0] + string.partition(i)[2]
        if i not in part.upper() and i not in part.lower():
            return i
            break
    else:
        return ''


print(first_non_repeating_letter('stress') == 't')

print(first_non_repeating_letter('moonmen') == 'e')

print(first_non_repeating_letter('abba') == '')

print(first_non_repeating_letter('~><#~><') == '#')

print(first_non_repeating_letter('hello world, eh?') == 'w')

print(first_non_repeating_letter('sTreSS') == 'T')

print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!') == ',')
