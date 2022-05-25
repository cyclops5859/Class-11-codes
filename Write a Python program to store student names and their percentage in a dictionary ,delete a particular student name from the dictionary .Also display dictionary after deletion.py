data = {}

while True :
    nam = input("Enter name : ")
    per = float(input("Enter percentage : "))
    data[nam] = per
    a = input("Do you want to enter more records enter (Y / N):")
    if a == "N" or a == "n":
        break
print (data)
clas = input("Enter name which you want to delete : ")
del data[clas]
print("Dictionary ",data)

