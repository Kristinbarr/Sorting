# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc (lines of code))

        # solution with FOR LOOP:
        # for cur_index in range(i+1, len(arr)):
        #     if arr[cur_index] < arr[smallest_index]:
        #         smallest_index = cur_index

        # WIP solution with while loop
        while cur_index < len(arr):
            # if left num is less, set it's index to small index
            if arr[cur_index] < arr[smallest_index]:
                smallest_index = cur_index
            #  iterate for the while loop
            cur_index += 1

        # TO-DO: swap
        # new destructuring swap method
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

        # previous swap method
        # temp = arr[i]
        # arr[i] = arr[smallest_index]
        # arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #instantiate swaped variable to true to enter while loop
    swaped = True

    while swaped:
        # reset swaped variable
        swaped = False
        # iterate through arr
        for i in range(0, len(arr)-1):
            # set variables for comparison nums
            first = arr[i]
            second = arr[i+1]
            # if right side is less than, swap
            if first > second:
                arr[i] = second
                arr[i+1] = first
                # since swap happened, set to True
                swaped = True

    return arr


# STRETCH: implement the Count Sort function below
# count sort is good for a small range of values
def count_sort( arr, maximum=-1 ):
    # iterate through arr and find range
    # create a new dict with range of values ex: 0-9
    # iterate through array and count up values into dict
    # reassign the dict value to itself and the value to the left(one int less)
    # create an empty duplicate arr with same length of the og
    # iterate through original array
    # place values of og array in the dict value

    return arr
