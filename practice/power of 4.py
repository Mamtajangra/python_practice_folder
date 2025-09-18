# we will find out power of 4 here 
def power_4(n):
    # firstly some edge cases like 0 and 1
    if n <= 0:
        return False
    # like 4**0 ==1
    if n == 1:
        return True
    # we will find out all the multiple of 4 /
    while n % 4 ==0:
        # now find out the numbers which are just only in power of 4 upto n==1 
        n = n//4
    if n ==1:
        # return true 
        return True
    # otherwise false 
    return False 


# example 
n = 16
print(power_4(n))



### similarly we can find out the power of 4,3,2,5,6 and so on .....
