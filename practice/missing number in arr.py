# we want to find out missing number in given array
def missing_num(arr):
    n = len(arr)
    # firstly we will sum up all elements of array 
    sum1 = sum(arr)
    # print(sum1)
    # this is the sum of n terms 
    total_sum = n*(n+1)//2
    # missing term =  total sum - sum of arr 
    missing_term = total_sum - sum1
    # return that term 
    return missing_term

# main 
arr = [3,0,1,4]
print(missing_num(arr))            ## but if the arr is [1,2,3,4,5,6,7,8,9....] we will use (n+1)*(n+2)//2 instead of n*(n+1)//2