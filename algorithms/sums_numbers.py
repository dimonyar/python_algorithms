# Adding up all the whole numbers from 1 through a given number n.

            # Example:
            # f(n=100) // returns 5050

# It's your duty to verify that n is a valid positive integer number. If not, please, return None


f = lambda n: sum(range(1, n + 1)) if type(n) == int and n > 0 else None

print(f(0))
print(f(100))
print(f(5.5))
