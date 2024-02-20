# 20/02/2024

# Write a Program to accept a number N and display whether it is positive
# Algorithm 
# 1) Accept N
# 2) If value of N is > 0, display "positive"
# 3) If value of N is < 0, display "Negetive"
# 4) stop

# program 

N = int(input("Enter a no:"))
if N > 0:
	print( N,"is positive")
elif N < 0:
	print (N,"is negetive")
else :
	print (N,"is Zero")
