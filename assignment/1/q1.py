#Python program to check whether the given integer is a multiple of both 5 and 7

def is_multiple_of_5_and_7(num):
        if num % 5 == 0 and num % 7 == 0:
        return True
    else:
        return False

user_input = int(input("Enter an integer: "))

if is_multiple_of_5_and_7(user_input):
    print(f"{user_input} is a multiple of both 5 and 7.")
else:
    print(f"{user_input} is not a multiple of both 5 and 7.")
