def prime_numbers(num):
   
    for i in num:
        if i <= 1:
            return False
        
        for nums in range(2, i):
                if i%nums==0:
                    return False
    return True     
print(prime_numbers([2,3,5,7]))               
print(prime_numbers([2,3,0,8])) 