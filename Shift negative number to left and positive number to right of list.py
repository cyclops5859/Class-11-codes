x=[-2,1,-3,-15,16,17,5,-3,6,-6]
y=[0]*10
a=len(x)
a=a-1
j=0

for i in range(10):
  if x[i]>0:
      y[j]=x[i]
      j+=1
     
  else:
      y[a]=x[i]
      a-=1
print(y)
