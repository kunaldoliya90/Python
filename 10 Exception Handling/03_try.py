try:
    # Prompt the user to input an integer
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    # Handle the ValueError exception if the input is not a valid integer
    print("Error: Invalid input. Please enter an integer.")
