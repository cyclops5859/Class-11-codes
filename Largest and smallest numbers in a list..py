# Q - Find the Largest and smallest numbers in a list.

x = []
e = int(input("Please enter the number of Elements: "))
for i in range(1, e + 1):
    value = int(input("Please enter the Value of the Element : "))
    x.append(value)

x.sort()

print("The Smallest Element in this List is : ", x[0])
print("The Largest Element in this List is : ", x[e - 1])
