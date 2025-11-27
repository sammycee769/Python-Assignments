def is_prime(number):
    if number <= 1:
        return False
    
    factors = 0

    for count in range(1, number + 1):
        if number % count == 0:
            factors += 1
    return factors == 2

def is_palindrome(number):
    original_number = number
    reverse = 0
    while (number > 0) :
        digit = number % 10;       
        reverse = reverse * 10 + digit; 
        number//= 10;          
        
    return reverse == original_number
def is_prime_is_palindrome(number):
    return is_prime(number) and is_palindrome(number) 
   
      
print (is_prime_is_palindrome(11))
