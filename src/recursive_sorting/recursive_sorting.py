# TO-DO: complete the helpe function below to merge 2 sorted arrays
import math
def merge( arrA, arrB ):
    merged_arr = []
    while len(arrA) > 0 and len(arrB) > 0:
        value = min(arrA[0], arrB[0])
        if value == arrA[0]:
            arrA.pop(0)
            merged_arr.append(value)
        else:
            arrB.pop(0)
            merged_arr.append(value)

    if len(arrA) > 0:
        for i in arrA:
            merged_arr.append(i)

    if len(arrB) > 0:
        for i in arrB:
            merged_arr.append(i)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        # divide
        left = merge_sort( arr[ 0: int(len(arr)//2) ] )
        right = merge_sort( arr[ int(len(arr)//2) :] )
        arr = merge(left, right)
    return arr

c = [2, 5, 3, 9, 0, 1]

print(merge_sort(c))




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
