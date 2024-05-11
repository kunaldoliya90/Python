def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a non-negative integer to find its factorial: "))
print("Factorial of", number, "is", factorial(number))
