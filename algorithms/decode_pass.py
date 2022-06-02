# Write a script that takes an array of possible passwords and a string of binary
# representing the possible password.Convert the binary to a string and compare
# to the password array. If the password is found, return the password string,
# else return false;

# decode_pass(['password123', 'admin', 'admin1'],'01110000 01100001 01110011 01110011 01110111 01101111 01110010
# 01100100 00110001 00110010 00110011');    => 'password123' decode_pass(['password321', 'admin', 'admin1'],
# '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011');    => False
# decode_pass(['password456', 'pass1', 'test12'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010
# 01100100 00110001 00110010 00110011');    => False


decode_pass = lambda pass_list, bits: (pas := ''.join(map(lambda x: chr(int(x, 2)), bits.split()))) in pass_list and pas


print(decode_pass(['password123', 'admin', 'admin1'],
                  '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'))
print(decode_pass(['password321', 'admin', 'admin1'],
                  '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'))
print(decode_pass(['password456', 'pass1', 'test12'],
                  '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'))
