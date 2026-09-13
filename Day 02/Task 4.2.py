result = 0

for i in range(999, 0, -2):
    result = i ** 2 / (6 + result)

pi = 3 + result

print(round(pi, 6))