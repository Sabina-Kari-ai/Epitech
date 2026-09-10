alphabet = "abcdefghijklmnopqrstuvwxyz"

message = input("Enter your message: ").lower()
key = input("Enter the key: ").lower()

result = ""
key_index = 0

for letter in message:
    if letter in alphabet:
        position = alphabet.index(letter)

        key_letter = key[key_index % len(key)]
        shift = alphabet.index(key_letter)

        new_position = (position + shift) % 26
        result += alphabet[new_position]

        key_index += 1
    else:
        result += letter

print(result)