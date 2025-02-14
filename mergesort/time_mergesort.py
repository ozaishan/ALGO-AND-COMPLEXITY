import random
import time
import sys
from mergesort import MERGESORT  

sys.setrecursionlimit(10**6)

def time_taken(arr):
    starttime = time.perf_counter_ns()
    MERGESORT(arr, 0, len(arr) - 1) 
    endtime = time.perf_counter_ns()
    return endtime - starttime

if __name__ == "__main__":
    sizes = [100, 300, 500, 700, 900, 1000, 1500, 2000, 3000, 5000]

    print("Benchmarking MergeSort:")
    for size in sizes:
        arr = list(range(size, 0, -1))  
        time_taken_ns = time_taken(arr)
        print(f"MergeSort on array of size {size}: {time_taken_ns} nanoseconds")


    print("\nBenchmarking MERGESort with shuffled arrays:")
    for size in sizes:
        arr = list(range(1, size + 1))  
        random.shuffle(arr)  
        time_taken_ns = time_taken(arr)
        print(f"MERGESORT on shuffled array of size {size}: {time_taken_ns} nanoseconds")