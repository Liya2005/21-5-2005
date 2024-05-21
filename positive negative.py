def count_positive_negative_numbers():
    n = int(input("Enter the value of n: "))
    positive_count = 0
    negative_count = 0
    i = 0

    while i < n:
        num = float(input(f"Enter number {i+1}: "))
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        i += 1

    return positive_count, negative_count

positive, negative = count_positive_negative_numbers()
print("Number of positive numbers:", positive)
print("Number of negative numbers:", negative)