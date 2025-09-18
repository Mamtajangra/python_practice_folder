# define a function 
def binary_search(arr,val_to_find):
    # low value 
    low = 0
    # high means the last index of array 
    high = len(arr) -1
    # loop because we don't know how many steps are required 
    while low <= high:
        # middle index is the half the sum of low and high value 
        mid_indx = (low + high)//2
        # check the conditions 
        if val_to_find == arr[mid_indx]:
            return mid_indx
        # again check the value is on left or right side 
        if val_to_find < arr[mid_indx]:
            high = mid_indx + 1

        else:
            low = mid_indx - 1


# main 
array = [12,22,23,34,44,56,67,77,89,88,90]
value = 89
print(binary_search(array,89))
