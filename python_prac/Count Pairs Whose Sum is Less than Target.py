# define a function and here we want to count the pairs ,there addition  gives the result  less than value
def count_pairs(arr,val):
    # suppose there is 0 pair initially 
    count = 0
    # loop over array 
    for i in range(len(arr)):
        # another loop start from next to i 
        for j in range(i+1,len(arr)):
        #   check the condition ...if this condition is fulfilled we count it a single 
            if arr[i] +  arr[j] < val:
                count = count+1
    return count  

# main 
arr = [-6,2,5,-2,-7,-1,3]
val = -2
print(count_pairs(arr,val))          

# (-6,2) = -4<-2  so count 
# (-6,5) = -1>-2  don't count similarly all values check in the same pattern 