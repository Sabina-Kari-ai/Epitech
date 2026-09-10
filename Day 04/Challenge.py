number, text = input("Enter a number and text: ").split(maxsplit=1)
number = int(number)
if number == 0:
    quit()

if any(v in text.lower() for v in "aeiou"):
    print(number)
elif number >= 42:
    print(number)
else:
    print(text)