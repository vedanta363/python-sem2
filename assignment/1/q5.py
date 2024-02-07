#Python program to find the sum of the digits of an integer using while loop
def sum_of_digits(num):
    total_sum = 0
    
    while num > 0:
        digit = num % 10
        total_sum += digit
        num = num // 10
    
    return total_sum

user_input = int(input("Enter an integer: "))

result = sum_of_digits(user_input)
print(f"The sum of the digits of {user_input} is: {result}")
