def find_nth_square_cube_number(n):
    count = 0
    num = 0

    while count < n:
        num += 1
        if num == pow(int(num ** (1/6)), 6):
            count += 1

    return num

n = int(input("Enter the value of n: "))

result = find_nth_square_cube_number(n)
print(f"The {n}-th number which is both a square and a cube is:", result)