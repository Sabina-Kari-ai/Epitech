def pal(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return pal(s[1:-1])

text = input("Text: ")
clean = ""

for x in text:
    if x.isalnum():
        clean += x.lower()

print(pal(clean))