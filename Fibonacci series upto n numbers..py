x = int(input("Enter any number:-"))
a = 0
b = 1
print("\n\nThe Fibonacci Series to",x,"is")
for i in range (1,x+1):
    print (a,end=' ')
    c = a + b
    a,b = b,c
