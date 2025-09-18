# here we will check the duplicates and give result in true and false 
def duplicate(nums):
    # sort the list 
    nums.sort()
    # check if length is one there is no duplicate item 
    if len(nums)==1:
        return False
    # loop over the range of list 
    for i in range(len(nums)):
        # check each with previous one and return true 
        if nums[i] == nums[i-1]:
            return True
    return False     

# main 
nums = [2,2,3,2,4,4]
print(duplicate(nums))