# here we are going to fill fizz buzz in the string 
def fizzbuzz(n):
    # firstly we will choose a list which is empty 
    M = []
    # using a loop over the integers 
    for i in range(1,n+1):
        # check the number is divisible by 3 and 5 both 
        if i%3==0 and i%5==0:
            M.append("FizzBuzz")
            # another condition is for 3 only 
        elif i%3==0:
            M.append("Fizz")
            # this condition is for 5 
        elif i%5==0:
            M.append("Buzz") 
            # to obtain all fizzbuzz in string 
        else:
            M.append(str(i))  
    return M         


# check 
n = 5
print(fizzbuzz(n))