data = {}

while True :
    nam = input("Enter name : ")
    phone = eval(input("Enter phone number : "))
    data[ nam ] = [ phone ]
    a = input("Do you want to enter more records enter (Y / N): ")
    if a == "N" or a == "n":
        break

for i in data :
    print()
    print ("Name : ", i )
    print("Phone : ", data[ i ][ 0 ] , "\t")
