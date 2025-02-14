import time
from linear_search import linear_search

def time_taken_linear_search(n):
    arr = list(range(1, n + 1))
    
    starttime = time.time()
    
    result = linear_search(arr, n)
    
    endtime = time.time()
    
    elapsed_time = endtime - starttime
    
    print(f"Result of linear search for target {n}: {result}")
    print(f"Time taken to search in an array of size {n}: {elapsed_time} seconds")

if __name__ == "__main__":
    sizes = [10000, 30000, 50000, 70000, 90000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000]
    for size in sizes:
        time_taken_linear_search(size)
