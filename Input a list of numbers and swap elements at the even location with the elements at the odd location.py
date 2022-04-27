x = []
num = int(input("Enter size of list :- "))
for n in range(num):
    numbers = int(input("Enter the element :- "))
    x.append(numbers)

print("List : ",x)
y=len(x)
if y%2!=0:
    y=y-1
for i in range(0,y,2):
    x[i],x[i+1]=x[i+1],x[i]
print("List after swapping :",x)
