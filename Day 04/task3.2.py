alphabet = "abcdefghijklmnopqrstuvwxyz"

message = input("Enter encrypted message: ").lower()
key = int(input("Enter the key: "))

result = ""
for letter in message:
    if letter in alphabet:
        position = alphabet.index(letter)
        new_position = (position - key) % 26
        result += alphabet[new_position]
    else:
        result += letter

print(result)