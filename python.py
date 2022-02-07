a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a>b and a>c:
    print("a is the largest")
elif b>a and b>c:
    print("b is the largest")
else:
    print("c is the largest ")



#calculating the salary
salary =int(input("Salary: "))
period=int(input("Period: "))
if period>=10:
    print(0.1*salary)
elif period>=6 and period<=10:
        print(0.08*salary)
elif period<6:
        print(0.05*salary)
 
 #Gettting average for each subject
 subject_one =int(input("Score: "))
subject_two=int(input("Score: "))
subject_three=int(input("Score: "))
subject_four =int(input("Score: "))
subject_five=int(input("Score: "))
average=(subject_one+subject_two +subject_three+subject_four+subject_five )/5
if average>=70 and average<=100:
     print("Grade A")
elif average>=60 and average<=69:
     print("Grade B")
elif average>=50 and average<=59:
     print("Grade C")
elif average>=40 and average<=49:
     print("Grade D")
elif average>=0 and average<=39:
     print("fail")
else:
    print("Invalid score")
