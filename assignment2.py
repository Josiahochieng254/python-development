#Entering the grading system
marks=int(input("Score: "))
if marks>=70 and marks<=100:
    print("A")
elif marks>=60 and marks<=69:
    print("B")
elif marks>=50 and marks<=59:
    print("C")
elif marks>=40 and marks<=49:
    print("D")
else:
    print("Fail")