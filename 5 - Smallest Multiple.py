# source: https://projecteuler.net/problem=5

number = 0
for number in range(2520, 1000000000, 20):
    flag = 1
    for i in range(20, 0, -1):
        if number % i > 0:
            flag = 0
            break
    if flag == 1:
        print("Answer: {number}")
        break
