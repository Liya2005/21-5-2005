def fibonacci_reverse(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    fib_series.reverse()
    return fib_series

n = int(input("Enter the number of terms in the Fibonacci series: "))
print("First", n, "terms of Fibonacci series in reverse order:")
print(fibonacci_reverse(n))