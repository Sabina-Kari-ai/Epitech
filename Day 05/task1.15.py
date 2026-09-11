print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])

x = [42, 3, 4, 18, 3, 10]
for number in x:
    if number % 2 == 0:
        print(number // 2)
    else:
        print(number * 2)