r = []
num = int(input("Enter size of list :- "))
for n in range(num):
    numbers = int(input("Enter the element :- "))
    r.append(numbers)
  
r.sort()
print ('list - ' ,r)
print("Third largest element in the list is:", r[-3])
