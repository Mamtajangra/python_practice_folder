# we are going to find out the addition of digits 
def add_digits(num):
    # if num=0 it gives the same output 
    if num ==0:
        return 0
    # the number is always greater than 10  because after 10 we will find out the sum of digits /
    while num>=10:
        # initialize sum is 0
        x = 0
        # convert number into string easy to find digits 
        for digits in str(num):
            # now sum is equal to the sum +digits again that string converted to integer 
            x = x+int(digits)
            # this sum become new number this time 
        num = x
# return num here 
    return num
# check 38 and after adition it gives 2
num = 38
print(add_digits(num))        


