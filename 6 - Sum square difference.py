# source: https://projecteuler.net/problem=6

start = 1
stop = 100
natural_numbers = range(start, stop+1)
square_natural_total = sum([x*x for x in natural_numbers])
natural_total_squared = pow(sum(natural_numbers), 2)

print(f"Answer: {natural_total_squared - square_natural_total}")

