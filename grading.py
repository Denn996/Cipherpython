#GRADE STUDENTS MARKS

#use the following grading system to grade students marks 70 and above = A, 60-69 = B, 50-59 = C, 40-49 = D, below 40 = Fail
marks = float(input("Enter marks: "))
if marks > 100 or marks < 0:
    print("invalid marks")

elif marks >= 70:
    print("A")

elif marks >= 60:
    print("B")

elif marks >= 50:
    print("C")

elif marks >= 40:
   print("D")

else:
    print("Fail")







