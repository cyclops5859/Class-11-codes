data = {}

while True :
    clas = int(input("Enter class : "))
    teach = input("Enter class teacher name : ")
    data[clas]= teach
    a = input("Do you want to enter more records enter (Y/N): ")
    if a == "N" or a == "n":
        break

clas = int(input("Enter class which you want to search : "))
print("class teacher name is : ",data[clas])
