"""
Create a function that takes a positive integer and returns the next bigger number
that can be formed by rearranging its digits. For example:

            12 ==> 21
            513 ==> 531
            2017 ==> 2071
            nextBigger(num: 12)   // returns 21
            nextBigger(num: 513)  // returns 531
            nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

            9 ==> -1
            111 ==> -1
            531 ==> -1
            nextBigger(num: 9)   // returns nil
            nextBigger(num: 111) // returns nil
            nextBigger(num: 531) // returns nil
"""


def next_bigger(n):
    lst = [i for i in str(n)]

    flag = False

    for i in range(len(lst) - 2, -1, -1):
        for c in range(i, len(lst))[::-1]:
            if lst[i] < lst[c]:
                lst[i], lst[c] = lst[c], lst[i]
                lst[i + 1:] = sorted(lst[i + 1:])
                return int(''.join(lst))
                flag = True
                break
        if flag:
            break
    else:
        return -1


print(next_bigger(46) == 64)
print(next_bigger(144) == 414)
print(next_bigger(95066793250158) == 95066793250185)
print(next_bigger(99774735383880) == 99774735388038)
print(next_bigger(9876543210) == -1)
