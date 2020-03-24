
def find_pivot(arr,min_pos,max_pos):

    if min_pos == max_pos:
        return min_pos

    mid = (min_pos + max_pos) // 2

    if arr[mid] <= arr[max_pos]:
        return find_pivot(arr,min_pos,mid)

    if arr[mid] >= arr[min_pos]:
        return find_pivot(arr,mid+1,max_pos)

array = [4,5,6,2,3]

print(find_pivot(array,0,len(array)-1))

def binary_search(arr,value,min,max):

    mid = (min + max) // 2

    if max < min:
        return -1

    if arr[mid] == value:
        return mid

    if value < mid:
        return binary_search(arr,value,min,mid)

    if value > mid:
        return binary_search(arr,value,mid,max)


def binary_search_rotated(arr,value):
    pivot = find_pivot(arr,0,len(arr)-1)

    if arr[pivot] == value:
        return pivot

    if arr[0] <= value:
        return binary_search(arr,value, 0, pivot - 1)
    return binary_search(arr,value, pivot + 1, len(arr) - 1)

print(binary_search_rotated(array,3))