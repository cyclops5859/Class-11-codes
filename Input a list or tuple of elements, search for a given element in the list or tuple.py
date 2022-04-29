x = []
num = int(input("Enter size of list :- "))
for n in range(num):
    numbers = int(input("Enter the element :- "))
    x.append(numbers)

r = int(input('Enter an element to be search : '))

for i in range(num):
    if r == x[i]:
        print("Element found at Index:", i)
