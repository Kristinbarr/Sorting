# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc

        for cur_index in range(cur_index+1, len(arr)):
            if arr[cur_index] < arr[smallest_index]:
                arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # edge case if arr is 0 or 1 element
    if len(arr) <= 1:
        return arr
    
    swapped = True

    # while something has been swapped
    while swapped is True:
        # set swap to false
        swapped = False
        # iterate through the arr and swap if needed
        for i in range(len(arr)-1):
            # if cur item is bigger than the next item, 
            if arr[i] > arr[i+1]:
                # swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # and set swap to true
                swapped = True

    return arr

    # TWO FOR LOOPS:
    # for i in range(len(arr) - 1, 0, -1):
    #     print(i)
    #     for j in range(i):
    #         if arr[j] > arr[j + 1]:
    #             arr[j], arr[j+1] = arr[j+1],arr[j]
    # return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
