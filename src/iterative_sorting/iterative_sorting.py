# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc (lines of code))

        smallestNum = arr[smallest_index]
        print('smallestNum', smallestNum)

        while smallest_index < len(arr):
            print('smallest index:', smallest_index)
            print('curEl...smallestEl: ', arr[cur_index], smallestNum)
            if (smallestNum > arr[smallest_index]):
                smallestNum = arr[smallest_index]
                print('NEW smallest: ', smallestNum)
            smallest_index += 1

        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = smallestNum
        arr[smallest_index] = temp

        print('NEW array:', arr)
        print()

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
