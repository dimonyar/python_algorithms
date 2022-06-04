"""
The goal of this exercise is to convert a string to a new string where each
character in the new string is "(" if that character appears only once in the
original string, or ")" if that character appears more than once in the original
string. Ignore capitalization when determining if a character is a duplicate.

        Examples

        "din"      =>  "((("
        "recede"   =>  "()()()"
        "Success"  =>  ")())())"
        "(( @"     =>  "))(("
Notes

Assertion messages may be unclear about what they display in some languages.
If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!
"""


def duplicate_encode(word):
    encod = ''
    for i in word:
        part = word.partition(i)[0] + word.partition(i)[2]
        if i not in part.upper() and i not in part.lower():
            encod += '('
        else:
            encod += ')'
    return encod


print(duplicate_encode("din") == "(((")

print(duplicate_encode("recede") == "()()()")

print(duplicate_encode("(( @") == "))((")
