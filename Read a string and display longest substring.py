str = "the yellow banana is sweeter than the green banana but the black banana is preffered by most of the people eating bananas"
print (str)
x  = (input("Enter First substring : "))
y  = (input("Enter Second substring : "))
count1 = str.count(x)
count2 = str.count(y)

if count1 > count2:
    print ('The first Substring is the longest')

else:
    print ('The second substring is the longest')
