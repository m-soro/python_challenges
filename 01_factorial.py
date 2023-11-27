# Returns the value of the factorial of num if it is defined, otherwise, returns None
def factorial(num):
    if isinstance(num,int) and num >= 0:
        if num == 0: 
            return 1
        return num * factorial(num-1)
    else: 
        return None
    
# return 120
print(factorial(5))    