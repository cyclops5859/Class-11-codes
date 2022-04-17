lst = [ 3, 13, 9, 12, 13, 30, 15, 9, 45, 36, 12, 12]
d = []
u = {}
for x in lst:
   if x not in u:
      u[x] = 1
   else:
      if u[x] == 1:
         d.append(x)
      u[x] += 1
print(d)
