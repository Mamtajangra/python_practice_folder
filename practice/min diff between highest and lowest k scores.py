# to find the diff between k scores we use sliding window here 
def min_diff(nums,K):
    # first of all sort the array
    nums.sort()
    # initialize i and j means the starting and ending point of a particular window 
    i = 0
    j = K-1
    # difference is below 
    diff = nums[j] - nums[i]
    # minimum diff is diff in initial stage 
    minimum_diff = diff
    # loop over the length -1 because it reaches faster
    while j <len(nums)-1:
        i = i+1
        j = j+1
        diff = nums[j] - nums[i]
        minimum_diff = min(diff,minimum_diff)
    return minimum_diff


# check 
nums = [9,4,1,7]
K= 2
print(min_diff(nums,K))