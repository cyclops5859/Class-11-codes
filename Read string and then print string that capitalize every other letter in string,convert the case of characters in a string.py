def word(string):
    nw = ""
    i = True
    for char in string:
        if i:
            nw += char.upper()
        else:
            nw += char.lower()
        if char != ' ':
            i = not i
    return nw
print(word("WelCoMe tO thE WorlD Of PyThoN!"))
