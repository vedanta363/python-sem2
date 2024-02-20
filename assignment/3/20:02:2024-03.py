# Accept marks of 3 subjects out of 100. Display total marks, percentage and grade. Calculate grade as following
# if percentage >= 70, grade "o"
# if percentage >= 60, grade "A"
# if percentage >= 50, grade "B"
# if percentage < 50, grade "F"

M1 = int(input("Enter 1st Subject Marks:"))
M2 = int(input("Enter 2nd Subject Marks:"))
M3 = int(input("Enter 3rd Subject Marks:"))

TM = M1+M2+M3
PerM = TM/3 
print("The total marks is : ", TM)
print ("The percentage is : ", PerM)

if PerM >= 70:
    print("The grade is : O")
elif PerM >= 60:
    print("The grade is : A")
elif PerM >= 50:
    print("The grade is : B")
else:
    print("The Grade is : F")
