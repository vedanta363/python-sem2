#Python program to display the given integer in reverse manner

def reverse_integer(num):
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    
    return reversed_num

user_input = int(input("Enter an integer: "))

result = reverse_integer(user_input)
print(f"The reverse of {user_input} is: {result}")
