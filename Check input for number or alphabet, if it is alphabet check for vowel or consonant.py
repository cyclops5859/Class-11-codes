ch = input("Please Enter Any Character : ")
 
if(ch.isdigit()):
    print("The Given Character ", ch, "is a Digit")

elif(ch.isalpha()):
    print("The Given Character ", ch, "is an Alphabet")

    if ch in ('a', 'e', 'i', 'o', 'u'):
        print("its is a vowel.")
    
    else:
	    print("its is a consonant.") 

else:
    print("The Given Character ", ch, "is a Special Character")
