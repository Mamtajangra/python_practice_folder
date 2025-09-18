# here we want to count all operations upto we get 0 result 
def count_op(num1,num2):
    # now we initialize count = 0
    count =0
    # we will check through loop 
    while num1>0 and num2>0:
        # if 1> 2 then we will subtract 2 from 1 store the result in num1
        if  num1 >= num2: 
            num1 = num1 - num2
            # here 2> 1 and store result to num2 
        else:
            num2 = num2 - num1
            # count the number of operations  to get result is zero 
        count = count +1 
    return count          


# check
num1 = 3
num2 = 2
print(count_op(num1,num2))


# - Operation 1: num1 = 2, num2 = 3. Since num1 < num2, we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1.
# - Operation 2: num1 = 2, num2 = 1. Since num1 > num2, we subtract num2 from num1.
# - Operation 3: num1 = 1, num2 = 1. Since num1 == num2, we subtract num2 from num1.
# Now num1 = 0 and num2 = 1. Since num1 == 0, we do not need to perform any further operations.
# So the total number of operations required is 3.