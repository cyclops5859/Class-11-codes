x = []
num = int(input("Enter size of list :- "))
for n in range(num):
    numbers = int(input("Enter the element :- "))
    x.append(numbers)

sum=0
for i in range(0,len(x)):
  sum=sum+pow(int(x[i]),3)

print("Sum of cube of digits  : ",sum)
if sum == x:
  print("Digits are matching to cube  : ", x)
else:
  print("Digits are NOT matching to cube : ", x)

print("Highest number : ",max(x))
print("Lowest  number : ",min(x))
