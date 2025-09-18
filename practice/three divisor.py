# we will findout three divisor of a number and return according to true and false 
def divisor(n):
    # initialize count is 0 
    count = 0
    # loop over the n 
    for i in range(1,n+1):
        # if any number completely divides the n we can start to count 
        if n % i ==0:
            count = count+1
            # return count 3 because we need just three count of a nummber
    return count == 3


n = 4
print(divisor(n))
