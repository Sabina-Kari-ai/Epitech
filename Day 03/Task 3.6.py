text = input("Enter text: ").lower()

letters = "abcdefghijklmnopqrstuvwxyzàâçéèêëîïôùûüÿ"

for letter in letters:
    if letter in text:
        print(letter, text.count(letter))