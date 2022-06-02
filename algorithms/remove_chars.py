# Let's assume we need "clean" strings. Clean means a string should only contain
# letters a-z, A-Z and spaces. We assume that there are no double spaces
# or line breaks.

# Write a function that takes a string and returns a string without the unnecessary
# characters.


remove_chars = lambda s: ''.join([i for i in s if i.isalpha() or i.isspace()])


print(remove_chars('my_list = ["a","b","c"]'))
print(remove_chars('john.dope@dopington.com'))
print(remove_chars('1 + 1 = 2'))
print(remove_chars("0123456789(.)+,|[]{}=@/~;^$'<>?-!*&:#%_"))
