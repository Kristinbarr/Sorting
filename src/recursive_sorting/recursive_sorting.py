# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # total of left + right items
    elements = len( arrA ) + len( arrB )
    # create an arr of placeholder items
    merged_arr = [None] * elements

    print('left', arrA)
    print('right', arrB)

    a = 0
    b = 0

    # for all elements:
    for i in range(elements):
        # # if arrA is merged, next el in arrB goes to merged arr
        # if a >= len(arrA):
        #     merged_arr[i] = arrB[b]
        #     b += 1
        # # elif arrB is merged, next el in arrA goes to merged arr
        # elif b >= len(arrB):
        #     merged_arr[i] = arrA[a]
        #     a += 1
        # # elif next el in arrA is smaller, add to merged arr
        # elif arrA[a] < arrB[b]:
        #     merged_arr[i] = arrA[a]
        #     a += 1

        # # elif next el in arrB is smaller, add to merged arr
        # else:
        #     merged_arr[i] = arrB[b]
        #     b += 1

        # attempting solution without subindexes
        # if length of both arrays are at least 1
        if len(arrA) and len(arrB):
            # compare first and second elements
            if arrA[0] < arrB[0]:
                pass


    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # base case
    if len(arr) <= 1:
        return arr

    # divide:
    if len(arr) > 1:
        # divide left: slice starting at 0, and splitting the right in half
        print('MERGE_SORT left', arr[0:len(arr) // 2])
        left = merge_sort( arr[0 : len(arr) // 2 ] )
        # right side is arr right half 
        print('MERGE SORT right', arr[ len(arr) // 2 : len(arr) ])
        right = merge_sort( arr[ len(arr) // 2 : ] )

    # merge peices together with merge()
    arr = merge(left, right)
    return arr


print(merge_sort([2, 1, 5, 4, 3]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end): 
    start2 = mid + 1; 
    # If the direct merge is already sorted 
    if (arr[mid] <= arr[start2]): 
        return
    # Two pointers to maintain start 
    # of both arrays to merge 
    while (start <= mid and start2 <= end): 
        # If element 1 is in right place 
        if (arr[start] <= arr[start2]): 
            start += 1; 
        else: 
            value = arr[start2]; 
            index = start2; 
            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while (index != start): 
                arr[index] = arr[index - 1]; 
                index -= 1; 
            arr[start] = value; 
            # Update all the pointers 
            start += 1; 
            mid += 1; 
            start2 += 1; 
    return
''' 
* l is for left index and r is right index of 
the sub-array of arr to be sorted 
'''
def merge_sort_in_place(arr, l, r): 
    if (l < r): 
        # Same as (l + r) / 2, but avoids overflow 
        # for large l and r 
        m = l + (r - l) // 2
        print(l,r)
        # Sort first and second halves 
        merge_sort_in_place(arr, l, m); 
        merge_sort_in_place(arr, m + 1, r); 
        merge_in_place(arr, l, m, r); 



# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
