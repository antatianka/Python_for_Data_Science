def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''    
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
            