# 10.4 Write a Python program that executes division and handles an
# ArithmeticError exception if there is an arithmetic error.
try:
    # Execute division
    result = 10 / 0
except ArithmeticError:
    # Handle the ArithmeticError exception
    print("Error: Arithmetic error occurred")
