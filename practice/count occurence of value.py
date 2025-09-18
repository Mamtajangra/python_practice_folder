# we will find out a value in the arr and its count also 
def occurrence(arr,val):
    # initially count is 0
    count = 0
    # using a loop over the array 
    for i in range(len(arr)):
        # check the condition if value is equal to any element in array 
        if val == arr[i]:
            # count the same value in array 
            count = count+1
    return count 

# 

arr = [1,2,1,2,1,3,4,5,6]
val = 1
print(occurrence(arr,val))