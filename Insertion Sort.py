r = []
num = int(input("Enter size of list :- "))
for n in range(num):
    numbers = int(input("Enter the element :- "))
    r.append(numbers)

print ("List before sorting :", r)
x = r.sort()
print ("List after sorting :", r)
