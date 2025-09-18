# here we want to sort a single element present in the array where all the elements occur twice so simply we use xor here
def sort_single(arr):
    # suppose result is zero initially 
    result = 0
    # using a loop over the array  
    for i in arr:
        # using xor to find single element 
        result ^= i
    return result 

# main 
arr = [1,2,1,2,3,3,4,8,4,5,6,5,6]
print(sort_single(arr))