# here we will find out a number and its double also present in the array 
def count_double(arr):
    # loop over the array length to pickup each index value 
    for i in range(len(arr)):
        # here check the values with previous one 
        for j in range(len(arr)):
            # this condition is must 
            if i!=j and arr[i] ==2*arr[j]:
                # if any element follow return true otherwise false 
                return True
    return False     


# array 
arr = [1,1,3,4,5,6,8]
print(count_double(arr))    