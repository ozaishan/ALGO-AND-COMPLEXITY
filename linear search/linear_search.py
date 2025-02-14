def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return target
    return -1
