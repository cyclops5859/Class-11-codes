list = [10, 20, 30, 40, 50, 60]

n = len(list)

if( n%2 != 0 ):
    print ("List has ODD number of elements.")
    exit()

else:
    list1 = list [0:3]
    list2 = list [3:n]
    print ("list : ",list)
    print ("list1: ",list2, list1)
