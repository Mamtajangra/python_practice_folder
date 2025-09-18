# here we will find out the fibonacci number 
def fib(n):
    # firstly according to series we check two conditions 
    if n==0:
        return 0
    # another for 1
    elif n == 1:
        return 1
    # initialize first two elements for fibonacci 
    n1 = 0
    n2 = 1
    # check all the elemnts over integers 
    for i in range(2,n+1):
        # swapping 
        n1,n2 = n2,n1+n2
    return n2

# check 
n = 4
print(fib(n)) ## 0,1,1,2,3,5,8
               ## n= 4 so, 3 exist 
                