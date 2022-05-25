print ('Using only 2 variables')
x = int(input('Enter first number : '))
y = int(input('Enter Second number : '))
print ("Before swapping: ")
print(x, y)
x, y = y, x
print ("After swapping: ")
print(x, y)
#-----Using 3 variables--------
print ('Using 3 variables')
a=int(input('Enter value : '))
b=int(input('Enter value : '))
print('Before swapping  :',a,b)
k=a
a=b
b=k
print('After swapping a becomes :',a,b)
