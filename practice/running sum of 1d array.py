# we are going to find out the running sum of 1d array
def running_sum(arr):
    # use an empty list to store the values
    M = []
    # initialize sum is 0
    sum = 0
    # use a loop over the array and find the sum of elements with the previous one
    for i in arr:
        sum = sum+i
        # append sum to list M 
        M.append(sum)
    return M

# CHECK 
array = [1,2,3,4] 
print(running_sum(array))   