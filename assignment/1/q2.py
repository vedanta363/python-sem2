#Python program to display all the multiples of 3 within the range 10 to 50

def display_multiples_of_3(start, end):
    print(f"Multiples of 3 within the range {start} to {end}:")
    for num in range(start, end + 1):
        if num % 3 == 0:
            print(num)

start_range = 10
end_range = 50

display_multiples_of_3(start_range, end_range)
