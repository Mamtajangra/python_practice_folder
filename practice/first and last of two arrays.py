def search(nums,target):
    def first(nums,target):
        first = -1
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if target == nums[mid]:
                first =  mid
                high = mid-1
            elif target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        return first   


    def last(nums,target):
        last = -1
        low =0              
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if target == nums[mid]:
                last =  mid
                low = mid +1
            elif target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        return last 
    first1=first(nums,target)
    last2 = last(nums,target)
    return(first1,last2)


nums = [5,7,7,8,8,10]
target = 8
result = search(nums,target)
print(result)