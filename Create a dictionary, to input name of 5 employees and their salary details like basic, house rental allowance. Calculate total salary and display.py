for i in range (5):
    name=input('Enter employee name: ')

    basic_salary=float(input('Basic salary : ')) 
    deduction=float(input('House rent : '))
    bonus=float(input('Bonus amount : '))
    totalsal=basic_salary+bonus-deduction  

    print(name,'total salary',totalsal)
