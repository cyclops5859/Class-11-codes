# Q4 - write a program to input the value of x and n and print the sum of the series.
x = eval(input("Enter the value of x : "))
n = eval(input("Enter the value of n : "))
f = 0
s = 0
t = 0
fo = 0
i=1
p =1
for i in range (n+1):
    f += x**i
print ("The sum of First series is",f)

for i in range (n+1):
    if i%2==0:
        s += x**i
    else:
        s -= x**i
print ("The sum of Second series is", s)

for i in range (n+1):
    if i%2==0:
        s += (x**i)/n
    else:
        s -= (x**i)/n
print ("The sum of Third series is",t)

for i in range (1,n+1):
    p=p*i
    if i%2==0:
        s += (x**i)/p
    else:
        s -= (x**i)/p
print ("The sum of fourth series is",fo)
