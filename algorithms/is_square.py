# Write a function that checks whether all elements in an array are square numbers.
# The function should be able to take any number of array elements.

# Your function should return true if all elements in the array are square numbers
# and false if not.

# An empty array should return undefined / None / nil. You can assume that all array
# elements will be positive integers.

            # Examples:

            # is_square([1, 4, 9, 16]) --> True

            # is_square([3, 4, 7, 9]) --> False

            # is_square([]) --> None

            # arr = [1, 4, 9, 16, 25]

def is_square(arr):
    return all(map(lambda x: pow(x, 1 / 2).is_integer(), arr)) if arr else None


print(is_square([]))
print(is_square([1, 4, 9, 16, 25, 36]))
print(is_square([1, 2, 3, 4, 5, 6]))
print(is_square([1, 2, 4, 15]))
