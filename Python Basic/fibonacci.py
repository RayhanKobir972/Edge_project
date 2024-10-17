num_terms = int(input("Enter the number of terms: "))

def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print(f"Fibonacci series up to {num_terms} terms: {fibonacci_series(num_terms)}")
