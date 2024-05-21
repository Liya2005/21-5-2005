def print_square_of_stars(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


size = 5
print_square_of_stars(size)