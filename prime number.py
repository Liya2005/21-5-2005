def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes_up_to_n(n):
    """Print all prime numbers up to n."""
    for num in range(2, n + 1):
        if is_prime(num):
            print(num, end=' ')


n = int(input("Enter the number up to which you want to print prime numbers: "))

print(f"Prime numbers up to {n}:")
print_primes_up_to_n(n)