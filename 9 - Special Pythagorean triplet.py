# source: https://projecteuler.net/problem=9
# note: The solution gets the right answer, but a not less than b :/

target = 1000

m = 2
n = 1
total = 0
found = 0
for n in range(1, 1000):
    for m in range(2, 1001):
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
        total = a + b + c
        if total == target:
            found = 1
            product = a * b * c
            print(f"Answer: {product}")
            print(a, b, c, (m, n))
            break
    if found:
        break

