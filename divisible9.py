def find_divisible_by_9(n, m):
    
    if n > m:
        n, m = m, n
    
   
    divisible_by_9 = []
    
  
    for i in range(n, m + 1):
        if i % 9 == 0:
            divisible_by_9.append(i)
    total_sum = sum(divisible_by_9)
   return divisible_by_9, total_sum
n = int(input("Enter the starting number (n): "))
m = int(input("Enter the ending number (m): "))
numbers, total_sum = find_divisible_by_9(n, m)
print(f"Numbers divisible by 9 between {n} and {m}: {numbers}")
print(f"Sum of numbers divisible by 9: {total_sum}")