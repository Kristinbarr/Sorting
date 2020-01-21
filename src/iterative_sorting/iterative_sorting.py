# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc (lines of code))

        # solution with FOR LOOP:
        # for j in range(i+1, len(arr)):
        #     if arr[j] < arr[smallest_index]:
        #         smallest_index = j

        # WIP solution with while loop
        while cur_index < len(arr):
            if arr[cur_index] < arr[smallest_index]:
                smallest_index = cur_index
            cur_index += 1

        # TO-DO: swap
        # new destructuring swap method
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

        # previous swap method
        # temp = arr[i]
        # arr[i] = arr[smallest_index]
        # arr[smallest_index] = temp

        print('NEW array:', arr)

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
