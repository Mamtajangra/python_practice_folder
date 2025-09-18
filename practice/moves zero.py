# we want to move eroes to right side 
def move_zero(nums):   
    # let position is zero initially  
    pos = 0
    # a loop over the length 
    for i in range(len(nums)):
        # if non zero elements are present swap with position 
        if nums[i] != 0:
            # swapping 
            nums[i],nums[pos] = nums[pos],nums[i]
            # add next one position 

# check 
nums = [0,1,3,2,0,7] 
move_zero(nums)
print(nums)          
            