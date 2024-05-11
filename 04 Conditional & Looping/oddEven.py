def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")

# Input number from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd
check_even_odd(number)
