def multiplication_table(n, m):
    for i in range(1, m+1):
        print(n, "x", i, "=", n*i)
n = 5
m = 10
multiplication_table(n, m)