
def check_triangle_validity(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if check_triangle_validity(a, b, c):
    print("The triangle with sides", a, ",", b, ",", c, "is valid.")
else:
    print("The triangle with sides", a, ",", b, ",", c, "is not valid.")
