def is_first_last_bits_set(num):
   
    return num > 0 and num & (num - 1) == 0 and bin(num).count('1') == 2

def print_numbers_with_first_last_bits_set(n):
    for num in range(1, n+1):
        if is_first_last_bits_set(num):
            print(num)

n = int(input("Enter a positive integer: "))
print("Numbers with first and last bits as the only