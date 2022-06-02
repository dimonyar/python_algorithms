# Implement a pseudo-encryption algorithm which given a string S and an integer N
# concatenates all the odd-indexed characters of S with all the even-indexed
# characters of S, this process should be repeated N times.

# Examples:

# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"

# Together with the encryption function, you should also implement a decryption
# function which reverses the process.

# If the string S is an empty value or the integer N is not positive,
# return the first argument without changes.


def decrypt(encrypted_text, n):
    for i in range(n):
        encrypted_text1 = ''
        for i in range(0, int(len(encrypted_text) / 2)):
            encrypted_text1 += (encrypted_text[int(len(encrypted_text) / 2):])[i]
            encrypted_text1 += (encrypted_text[:int(len(encrypted_text) / 2)])[i]
        if len(encrypted_text) % 2 != 0:
            encrypted_text1 += encrypted_text[-1]
        encrypted_text = encrypted_text1
    return encrypted_text


def encrypt(text, n):
    for i in range(n):
        text1 = ''
        for i in range(len(text)):
            if i % 2 != 0:
                text1 += text[i]
        for i in range(len(text)):
            if i % 2 == 0:
                text1 += text[i]
        text = text1
    return text


print(encrypt("This is a test!", 3))

print(decrypt(encrypt("This is a test!", 3), 3))

print(encrypt("This kata is very interesting!", 1))

print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1))
