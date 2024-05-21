def fibonacci_series(n):
    """Generate and print the Fibonacci series up to N numbers."""
    if n <= 0:
        print("The number of terms must be positive.")
        return
    elif n == 1:
        print("Fibonacci series up to 1 term: 0")
        return
    elif n == 2:
        print("Fibonacci series up to 2 terms: 0 1")
        return
  
    a, b = 0, 1
    print(f"Fibonacci series up to {n} terms:", end=" ")
    print(a, b, end=" ")
    
    
    for _ in range(2, n):
        next_number = a + b
        print(next_number, end=" ")
        a, b = b, next_number
    print()  # For a new line at the end


n = int(input("Enter the number of terms for the Fibonacci series: "))


fibonacci_series(n)