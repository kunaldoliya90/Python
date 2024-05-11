def display_day(number):
    if number == 1:
        print("Monday")
    elif number == 2:
        print("Tuesday")
    elif number == 3:
        print("Wednesday")
    elif number == 4:
        print("Thursday")
    elif number == 5:
        print("Friday")
    elif number == 6:
        print("Saturday")
    elif number == 7:
        print("Sunday")
    else:
        print("Invalid input! Please enter a number between 1 and 7.")

# Input number from the user
number = int(input("Enter a number (1-7) representing a day of the week: "))

# Display the corresponding day
display_day(number)
