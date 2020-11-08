# source: https://projecteuler.net/problem=10

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


total = 2
for i in range(1, 2000000, 2):
    if is_prime(i):
        total += i
        print(i)
print(f"Answer: {total}")