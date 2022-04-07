# Q - Find whether a string is a palindrome or not. 
a = input("Enter a string : ")
b = a[::-1]

if a == b:
    print ('Yes it is palindrome!')

else:
    print ('No its not a palindrome!')
