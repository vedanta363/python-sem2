#Python program to display all integers within the range 100-200 whose sum of digits is an even number

def is_sum_of_digits_even(num):
    digit_sum = sum(int(digit) for digit in str(num))

    return digit_sum % 2 == 0

print("Integers in the range 100 to 200 with even sum of digits:")
for num in range(100, 201):
    if is_sum_of_digits_even(num):
        print(num)
      
