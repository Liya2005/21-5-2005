def prime_factors_product(n):
    
    product = 1
    
   
    divisor = 2
    
    
    while n > 1:
       
        if n % divisor == 0:
           
            product *= divisor
            
         
            while n % divisor == 0:
                n //= divisor
        
       
        divisor += 1
        
    return product
n = 36
print("Product of unique prime factors of", n, ":", prime_factors_product(n))