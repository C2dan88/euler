# source: https://projecteuler.net/problem=2

def gen_finbonacci_terms(largest_value):
    terms = [0, 1]
    _n = 0
    while _n <= largest_value:
        _n = sum(terms[-2:])  # add last two numbers in array together to get next term
        terms.append(_n)
    return terms


total = 0
for x in gen_finbonacci_terms(4000000):
    if x % 2 == 0:
        total += x

print(f"Awnser: {total}")
