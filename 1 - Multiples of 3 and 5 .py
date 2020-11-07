# source: https://projecteuler.net/problem=1

def is_multiple_of(num, multi):
    return num % multi == 0


total = 0
for i in range(1, 1000):
    if is_multiple_of(i, 3) or is_multiple_of(i, 5):
        total += i

print(f"Answer: {total}")