import time
from binary_search import binary_search

def timetaken_binary_search(n):
    arr = list(range(1, n + 1))
    
    starttime = time.time()
    
    result = binary_search(arr, n)
    
    endtime = time.time()
    
    timetaken = endtime - starttime
    
    print(f"Binary search result for target {n}: {result}")
    print(f"Time taken to search in an array of size {n}: {timetaken} seconds")

if __name__ == "__main__":
    sizes = [10]
    for size in sizes:
        timetaken_binary_search(size)
