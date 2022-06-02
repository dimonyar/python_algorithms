""" Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

            Example:

            ['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

            ["a","b","c","d","f"] -> "e"
            ["O","Q","R","S"] -> "P"
(Use the English alphabet with 26 letters!) """

def find_missing_letter(chars):
    import string

    alpha = string.ascii_letters
    start = alpha.find(chars[0])

    for i in range(1, len(chars)):
        start += 1
        if chars[i] != alpha[start]:
            return alpha[start]
            break


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']) == 'e')
print(find_missing_letter(['O', 'Q', 'R', 'S']) == 'P')
