def sorted(arr1,arr2,m,n):
    # m = len(arr1)
    # n = len(arr2)

    i = m-1
    j = n-1
    k = m+n - 1

    while i>=0 and j>=0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i = i-1

        else:
            arr1[k] = arr2[j]
            j = j-1
        k= k-1    

    while j >=0:
        arr1[k] = arr2[j]
        j = j-1
        k = k-1



arr1 = [1,2,2,1,3]
arr2 = [2,3,5,7]
