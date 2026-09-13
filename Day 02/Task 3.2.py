number = 123456789
result = 0

while number > 0:
    result += number % 10
    number //= 10

print(result)

number = 112233445566778899
result = 0

while number > 0:
    result += number % 10
    number //= 10

print(result)

number = 123456789 * 987654321
result = 0

while number> 0:
    result += number % 10
    number //= 10

print(result)