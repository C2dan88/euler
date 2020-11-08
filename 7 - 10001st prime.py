# source: https://projecteuler.net/problem=7


def is_prime(n):
    if n < 2:
        return False

    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False

    return prime


count = 1
target = 10001
i = 0
while count <= target:
    i += 1
    if is_prime(i):
        count += 1

print(f"Answer: {i}")
