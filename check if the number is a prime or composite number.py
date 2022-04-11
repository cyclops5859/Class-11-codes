# Q - Input a number and check if the number is a prime or composite number 
n= int(input("Enter any number:"))
if (n == 0 or n == 1):
    print(n,"Number is neither prime nor composite")
elif n>1 :
    for i in range(2,n):
        if(n%i == 0):
            print(n,"number is a composite number")
            break
    else:
        print(n,"number is a prime number")
else :
    print("Error")
