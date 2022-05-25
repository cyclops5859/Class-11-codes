r = []
 
num = int(input("Enter size of list :- "))
 
for n in range(num):

    numbers = int(input("Enter the element :- "))
    r.append(numbers)

x = int(input("Enter number to search in list :- "))
g =  (r.index(x))

print ("The number exists at :", g)
