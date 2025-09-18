# here we will find out intersection of two arrays where memory space is low and out of them one is in disk we cannot load all elements at the same time 
def intersection_arr(arr1,arr2):
    # firstly sort the both arrays
    arr1.sort()
    arr2.sort()
    # now initialize i and j means the indices of both arrays respectively 
    i= 0
    j = 0
    # initialize an empty list also 
    M= []
    # using while loop here because we don't know the exact number of times to check both arrays 
    while i< len(arr1) and j< len(arr2):
        # and = because if one of them condition is false loop stop 
        if arr1[i] == arr2[j]:
            M.append(arr1[i])
            # After checking elements, each index moving to the  next one  
            i = i+1
            j = j+1
            # if in case value of  i<j then we move to the next number       
        elif arr1[i] < arr2[j]:
            i = i+1
        else: 
        # similarly in j 
            j = j+1

    return M                
        
arr1 = [1,2,1,2,3,5,4]
arr2 = [5,4,6,2,3,8]
print(intersection_arr(arr1,arr2))
