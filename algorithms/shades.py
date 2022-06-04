"""
Write a function that takes a number n as a parameter and return an array containing
n shades of grey in hexadecimal code (#aaaaaa for example). The array should be sorted in ascending order starting
with '#010101', '#020202', etc. (using lower case letters).

            Examples:

            n =  1:    ["#010101"]
            n = 10:    ["#010101", "#020202", "#030303", "#040404", "#050505",
                        "#060606", "#070707", "#080808", "#090909", "#0a0a0a"]

As a reminder, the grey color is composed by the same number of red, green and blue:
#010101, #aeaeae, or #555555.

Black: #000000 and white: #ffffff are not accepted values.

When n is negative, just return an empty array. If n is higher than 254,
just return an array of 254 elements.

def shades_of_grey(n):
    if n > 254:
        n = 254
    return [('#'+ '%02x' % i * 3) for i in range(1,n+1)]
"""


def shades_of_grey(n):
    return [('#' + '%02x' % i * 3) for i in range(1, min(n + 1, 255))]


print(shades_of_grey(1))
print(shades_of_grey(10))
print(shades_of_grey(300))
