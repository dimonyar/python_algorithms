""" Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

            array = [[1,2,3],
                    [4,5,6],
                    [7,8,9]]
            snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

            array = [[1,2,3],
                    [8,9,4],
                    [7,6,5]]
            snail(array) #=> [1,2,3,4,5,6,7,8,9]
NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]]."""


def snail(snail_map):
    snail = []
    while len(snail_map) >= 2:
        snail.extend([i for i in snail_map[0]])
        snail_map.pop(0)

        snail.extend([i.pop() for i in snail_map])

        snail.extend([i for i in snail_map[-1][::-1]])
        snail_map.pop(-1)

        snail.extend([i.pop(0) for i in snail_map[::-1]])

    if len(snail_map) == 1:
        snail.extend([i for i in snail_map[0]])
    return snail


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(snail(array) == expected)

array = [[1, 2, 3, 4, 5, 6],
         [20, 21, 22, 23, 24, 7],
         [19, 32, 33, 34, 25, 8],
         [18, 31, 36, 35, 26, 9],
         [17, 30, 29, 28, 27, 10],
         [16, 15, 14, 13, 12, 11]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32, 33, 34, 35, 36]
print(snail(array) == expected)
