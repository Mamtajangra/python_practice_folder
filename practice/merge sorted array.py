# define a function here we want to merge two arrays in first array
def merge_sorted(nums1,m,nums2):  
        # m = len(nums1) 
        n = len(nums2) 
        # taking from last index    
        i = m-1
        j = n-1
        M =[]
        while i>=0 and j>=0:
            # check whether nums1[i] greater or not 
            if nums1[i] > nums2[j]:
                # i = i-1
                M.append(nums1[i])
                i = i-1
            else:
                M.append(nums2[j])
                j=j-1

                # if there is some elements left in array 
        while i>=0:
            M.append(nums1[i])
            i = i-1      ## it shows the decrement because values are assigning fromleft to right      
        while j>=0:
            M.append(nums2[j])
            j = j-1 

            # print M HERE 
            print(M) 
            # then we reverse the string because  values are from left to right  
        M.reverse()
        print(M)
        # here we will append all values in nums1 checking each element 
        for k in range(len(M)):
            nums1[k] = M[k]    
# main 
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m =3
print(merge_sorted(nums1,m,nums2))