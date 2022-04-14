x = int(input("Enter number of students: "))  
result = {}  
for i in range(x):  
   print("Enter Details of student No.", i+1)  
   roll = int(input("Roll No: "))  
   name = input("Student Name: ")  
   marks = int(input("Marks: "))  
   result[roll] = [name, marks]    
print(result)  

for student in result:  
   if result[student][1] > 75:  
       print("Student's name who get more than 75 marks is ",(result[student][0]))
