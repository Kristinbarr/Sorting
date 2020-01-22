# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    total_elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    # starting at beginning of `a` and `b`
    # compare the next value of each
    if arrA[0] <= arrB[0]:
        # add smallest to `merged_arr`
        merged_arr.append(arrA[0])
        merged_arr.append(arrB[0])
    else:
        merged_arr.append(arrB[0])
        merged_arr.append(arrA[0])

    print('HELPER MERGED ARR:', merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) > 1:
        left = arr[:len(arr) // 2] # slice to get left half
        right = arr[len(arr) // 2:] # slice to get right half



        # recursively call merge_sort() on LHS
        # recursively call merge_sort() on RHS
        # merge sorted pieces

    # divide array in half until there are subarrays of length 1
    # compare smaller left values of pairs
    # move smaller value to new array
    # compare smaller left values of pairs again
    # move smaller value to new array
    # when only one value, add that array to the end of the new arr
    # merge sorted lists together

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
