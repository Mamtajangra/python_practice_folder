# define a function 
def first_last(arr,val_to_find):
    # suppose these elements are not present in array so keep them -1
    first = -1
    last = -1
    # loop over entire length 
    for i in range(len(arr)):
        # check the condition value = array[i] 
        if val_to_find == arr[i]:
            # if that value find at any position assign it first 
            if first == -1:
                # return first 
                first = i
                # similarly if same find at last 
            last = i


    return(first,last) 

# main 
array = [12,21,23,43,45,22,33,56,44,22,12,12,11]
val_to_find = 22

first,last = first_last(array,val_to_find) 
print("first:",first,"last:",last)          