# Accept N1, N2
# Accept operator (+,-,*,/)
# if operator + then N1+N2

N1 = int(input("Enter 1st no:"))
N2 = int(input("Enter 2nd no:"))
op = input("Enter Operator(+,-,*,/,all)")

if op == "+":
    print ("Sum is", N1+N2)
elif op == "-":
    print ("Difference is ", N1-N2)
elif op == "*":
    print ("Product is",N1*N2)
elif op == "/":
    print ("divided is", N1/N2)
elif op == "all":
    print ("Sum is", N1+N2)
    print ("Difference is ", N1-N2)
    print ("Product is",N1*N2)
    print ("divided is", N1/N2)
else:
    print ("Wrong Operator Input ")