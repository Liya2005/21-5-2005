def extract_last_two_digits(n):
    if len(str(n)) <= 2:
        return "Number of digits should be greater than 2."
    else:
        last_two_digits = n % 100
        return last_two_digits


number = int(input("Enter an integer (greater than 2 digits): "))

result = extract_last_two_digits(number)
print("Last two digits of", number, "are:", result)
