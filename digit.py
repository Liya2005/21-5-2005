def find_nth_number(n, k):
    count = 0
    num = 0

    while count < n:
        num += 1
        if str(k) in str(num) or num % k == 0:
            count += 1

    return num

n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k (between 2 and 9): "))

result = find_nth_number(n, k)
print(f"The {n}-th number containing digit {k} or divisible by {k} is:", result)