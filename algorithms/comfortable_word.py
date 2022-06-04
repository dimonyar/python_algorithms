
"""
A comfortable word is a word which you can type always alternating the hand you
type with (assuming you type using a QWERTY keyboard).

That being said, complete the function which receives a word and returns true
if it's a comfortable word and false otherwise.

The word will always be a string consisting of only ascii letters from a to z.

To avoid problems with image availability, here's the lists of letters for each hand:

Left: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
Right: y, u, i, o, p, h, j, k, l, n, m
"""


def comfortable_word(word):
    right = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']

    return all((a in right) - (b in right) for a, b in zip(word, word[1:]))


def test_comfortable_word():
    assert comfortable_word('yams') is True
    assert comfortable_word('test') is False
    return print('All tests from comfortable_word passed successfully')
