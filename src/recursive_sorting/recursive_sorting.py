# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    total_elements = len(left) + len(right)
    merged_arr = [0] * total_elements
    # TO-DO
    # create indexes to iterate through each side's
    a = 0
    b = 0

    # starting at beginning of `a` and `b`
    for i in range(0, total_elements):

        if a >= len(left): # if there are no more elements in left side
            merged_arr[i] = right[b] # merge from right side
            b += 1

        elif b >= len(right): # if no elements in right side
            merged_arr[i] = left[a] # merge from left side
            a += 1

        elif left[a] < right[b]: # check 1st el in lists for greater el
            merged_arr[i]= left[a]
            a += 1

        else: # else case if right element is greater then left
            merged_arr[i] = right[b]
            b += 1
        # compare the next value of each
            # add smallest to `merged_arr`

    print('HELPER MERGED ARR:', merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) > 1:
        left = arr[:len(arr) // 2] # slice to get left half
        right = arr[len(arr) // 2:] # slice to get right half

        # recursively call merge_sort() on LHS
        print("left", left)
        left = merge_sort(left)
        # recursively call merge_sort() on RHS
        print("right", right)
        right = merge_sort(right)
        # merge sorted pieces
        return merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
