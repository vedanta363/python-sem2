#To check whether a given number is an Armstrong number or not in Python
def is_armstrong_number(number):
    order = len(str(number))
    temp = number
    sum_of_digits = 0

    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit ** order
        temp //= 10

    return number == sum_of_digits

user_input = int(input("Enter a number: "))

if is_armstrong_number(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")
