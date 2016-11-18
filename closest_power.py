def closest_power(base, num):
    
    check_number = {}
    exponent = 0
    
    while True:
        closest_number = base**exponent
        
        difference = abs(num-closest_number)
        
        if difference == 0:
            return exponent
            
        check_number[exponent] = difference
        
        min_difference = min(check_number.values())
        
        
        
        if min_difference < difference:
            exponent = [k for k, v in check_number.items() if v == min_difference]
            return exponent[0]
        else:
            
            exponent +=1
       
            
            
        
        
            
         
         
print closest_power(3,12)             
            