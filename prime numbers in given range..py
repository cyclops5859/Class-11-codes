# Q - Print prime numbers in given range. 
l=int(input('Enter the lowerlimit : '))
u=int(input('Enter the Upperlimit : '))
prime=1
for p in range(l, u+1):
	for i in range(2, int(p/2)+1):
		if(p%i==0):
			prime=0
			break
	if(prime==1):
		print(p)
	prime=1	
