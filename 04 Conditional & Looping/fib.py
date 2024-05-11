def fibonacci_series(n):
    fibonacci_seq = []
    a, b = 0, 1
    while a < n:
        fibonacci_seq.append(a)
        a, b = b, a + b
    return fibonacci_seq

# Get the Fibonacci series between 0 and 50
fibonacci_series_50 = fibonacci_series(50)

# Print the Fibonacci series
print("Fibonacci series between 0 and 50:")
print(fibonacci_series_50)
