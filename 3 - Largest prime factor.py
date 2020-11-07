# source: https://projecteuler.net/problem=3

def is_prime(n):
    if n < 2:
        return False

    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False

    return prime


x = 600851475143
largest_factor = 0
for i in range(1, 10000):
    if is_prime(i):
        if x % i == 0 and i > largest_factor:
            largest_factor = i

print(f"Awnser: {largest_factor}")
