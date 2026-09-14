text = input("Text: ").lower()

words = ["cat", "garden", "mice"]
total = 0

for word in words:
    total += text.count(word)
    total += text.count(word[::-1])

print(total)