try:
    # Code that may raise an exception
    x = 10 / 0
except ZeroDivisionError:
    # Handling the specific exception
    print("Error: Division by zero occurred")
finally:
    # Code that will always execute, regardless of whether an exception occurred
    print("Finally block executed")
