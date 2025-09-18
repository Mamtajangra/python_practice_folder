# here we want to determine a code in which we will count the pair whose sum is less than targrt 
def count_pair(arr,target):
    # initialize count =  0
    count = 0
    # loop over the array 
    for i in range(len(arr)):
        # loop start from i+1 
        for j in range(i+1,len(arr)):
            # check the condition 
            if arr[i] +arr[j] < target:
                # count each pair 
                count = count+1
    return count


# main 
arr = [-6,2,5,-2,-7,-1,3]
val = -2
print(count_pair(arr,val))  