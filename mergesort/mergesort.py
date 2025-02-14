
def MERGESORT(ARR, p, r):
    if p < r:
        q = (p + r) // 2
        MERGESORT(ARR, p, q)
        MERGESORT(ARR, q + 1, r)
        merge(ARR, p, q, r)

def merge(ARR, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = ARR[p + i]
    for j in range(n2):
        R[j] = ARR[q + 1 + j]
    
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            ARR[k] = L[i]
            i = i + 1
        else:
            ARR[k] = R[j]
            j = j + 1