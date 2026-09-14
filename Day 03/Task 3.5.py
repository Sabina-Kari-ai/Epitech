text = input("Enter text: ").lower()

for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter in text:
        print(letter, text.count(letter))

english = text.count("t") + text.count("h") + text.count("w")
french = text.count("e") + text.count("u") + text.count("q")

if english > french:
    print("Language: English")
else:
    print("Language: French")