try:
    # Code that may raise an exception
    x = 10 / 0
except ZeroDivisionError:
    # Handling the specific exception
    print("Error: Division by zero occurred")

# This code will not be executed if an exception occurs above
print("This statement will not be reached due to abnormal termination")
