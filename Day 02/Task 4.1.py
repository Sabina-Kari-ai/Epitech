result = 0
sign = 1

for i in range(5000000):
    result += sign / (2 * i +1)
    sign *= -1

pi = 4 * result

print(round(pi, 6))