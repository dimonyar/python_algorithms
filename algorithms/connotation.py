# You will be given a string with sets of characters, (i.e. words), seperated by
# between one and three spaces (inclusive).

# Looking at the first letter of each word (case insensitive-"A" and "a" should
# be treated the same), you need to determine whether it falls into the positive/first
# half of the alphabet ("a"-"m") or the negative/second half ("n"-"z").

# Return True/true if there are more (or equal) positive words than negative words,
# False/false otherwise.

# "A big brown fox caught a bad rabbit" => True/true
# "Xylophones can obtain Xenon." => False/false

def connotation(strng):
    return sum(strng < 'n' for strng in strng.lower().split()) >= sum(
        strng > 'n' for strng in strng.lower().split())


def test_connotation():
    result = connotation('All FOoD tAsTEs NIcE for someONe')
    assert result is True, f'Wrong result {result}'
    result = connotation('Xylophones can obtain Xenon.')
    assert result is False, f'Wrong result {result}'
    return print('All tests from connotation passed successfully')
