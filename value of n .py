def sum_of_n_numbers(n):
    sum = 0
    count = 1
    
    while count <= n:
        num = int(input("Enter number " + str(count) + ": "))
        sum += num
        count += 1
    
    return sum

n = int(input("Enter the value of n: "))
result = sum_of_n_numbers(n)
print("Sum of", n, "numbers is:", result)