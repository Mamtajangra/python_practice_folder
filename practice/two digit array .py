# we are moving to solve a problem where we will firstly find minimum from two arrays and make a two digit number from them
def two_digit(nums1,nums2):
    # if there is a common value in both arrays we will find out this value via converting list to set and intersection further 
    common = set(nums1) & set(nums2)
    # return minimum value from common 
    if common:
        return min(common)
    
 # firstly find out the minimum value from nums1 and nums2 
    x = min(nums1)
    y = min(nums2)
    # it is two digit number 
    return min(x*10 + y,y*10 +x)


nums1 = [4,1,3]
nums2 = [5,7]
print(two_digit(nums1,nums2))
    