# here we want to find any value and sort the same list so firstly define a function 
def list_sort(arr,val):
    # firstly we will sort the list 
    arr.sort()
    # taking an empty list here 
    M = []
    # now we use a loop over the lenth of array
    for i in range(len(arr)):
        # check the condition 
        if val == arr[i]:
            # append to list 
            M.append(i)

    return M     

arr = [1,2,5,7,6,9,4,2,6,2,2,0]
val = 2
print(list_sort(arr,val))   