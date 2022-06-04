"""
Given a string, return true if the first instance of "x" in the string is immediately followed by the string "xx".

            tripleX("abraxxxas") → true
            tripleX("xoxotrololololololoxxx") → false
            tripleX("softX kitty, warm kitty, xxxxx") → true
            tripleX("softx kitty, warm kitty, xxxxx") → false
Note :

capital X's do not count as an occurrence of "x".
if there are no "x"'s then return false
"""


def triple_x(s):
    return s.find('x') == s.find('xxx') != -1


print(triple_x(""))
print(triple_x("there's no XXX here"))
print(triple_x("abraxxxas"))
print(triple_x("xoxotrololololololoxxx"))
print(triple_x("soft kitty, warm kitty, xxxxx"))
print(triple_x("softx kitty, warm kitty, xxxxx"))
print(triple_x("soft kitty, warm kitty, x"))
