# here we will find the sum of elements present in any array < target and trying to eliminate indicies
def two_sum(arr,target):
    # using a loop over the length of array to check all values 
    for i in range(len(arr)):
        # this loop starts from the next element of i 
        for j in range(i+1,len(arr)):
            # check the condition now  sum of two values equal to the target 
            if arr[i] +arr[j] == target:
                return[i,j]
            
# example 
array = [2,7,11,15]    
target = 9
print(two_sum(array,target))        
