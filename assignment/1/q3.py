#Python program to find the average of 10 numbers using while loop

total = 0
count = 0

while count < 10:
    try:
        num = float(input(f"Enter number {count + 1}: "))
        
        total += num

        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid number.")

average = total / 10

print(f"The average of the 10 numbers is: {average}")
