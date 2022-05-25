text = input("Enter a string : ")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
newtext = ""

for i in text:
    if i not in vowels:
        newtext = newtext + i

print("With Vowels =", text)
text = newtext
print("Without Vowels =", text)
