alphabet = "abcdefghijklmnopqrstuvwxyz"

freq = [
    8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0,
    6.1, 7.0, 0.15, 0.77, 4.0, 2.4,
    6.7, 7.5, 1.9, 0.095, 6.0, 6.3,
    9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074
]

text = input("Encrypted text: ").lower()
key_length = int(input("Key length: "))

letters = [c for c in text if c in alphabet]
key = ""

for k in range(key_length):
    column = letters[k::key_length]

    best_shift = 0
    best_score = float("inf")

    for shift in range(26):
        score = 0

        for i in range(26):
            count = 0

            for letter in column:
                if (alphabet.index(letter) - shift) % 26 == i:
                    count += 1

            expected = len(column) * freq[i] / 100

            if expected > 0:
                score += (count - expected) ** 2 / expected

        if score < best_score:
            best_score = score
            best_shift = shift

    key += alphabet[best_shift]

print("Key:", key)