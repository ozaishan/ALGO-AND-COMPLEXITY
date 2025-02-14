def QUICKSORT(Arr, p, r):
    if p < r:
        q = PARTITION(Arr, p, r)
        QUICKSORT(Arr, p, q - 1)
        QUICKSORT(Arr, q + 1, r)

def PARTITION(Arr, p, r):
    x = Arr[r]  # Pivot element
    i = p - 1
    for j in range(p, r):
        if Arr[j] <= x:
            i = i+1
            
            Arr[i], Arr[j] = Arr[j], Arr[i]
    Arr[i + 1], Arr[r] = Arr[r], Arr[i + 1]
    return i + 1
