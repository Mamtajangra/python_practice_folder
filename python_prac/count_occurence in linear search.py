# define a function 
def occurrence_count(arr, val_to_find):
# initialize starting count is 0
    count = 0
    # loop over the length of array 
    for i in range(len(arr)):
        # check condition firstly 
        if val_to_find == arr[i]:
            # add each count 
            count = count + 1
    return count   



array = [1,3,2,66,44,2,4,6,8,5,6,5,6,9,87]
value = 6
result = occurrence_count(array,value)

print("value_occurrence",result,"times.")

