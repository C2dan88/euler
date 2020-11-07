# source: https://projecteuler.net/problem=4

def is_palindrome(digits):
    return str(digits) == str(digits)[::-1]

max_range = 999
found = False
terms = []
for x1 in range(max_range, 99, -1):
    for x2 in range(max_range, 99, -1):
        number = x1 * x2
        if is_palindrome(number):
            terms.append(number)

#print(terms)
print(f"Answer: {max(terms)}")
