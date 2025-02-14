import time
from insertionsort import insertion_sort

def time_taken(sort_function, arr):
    starttime = time.perf_counter_ns()
    sort_function(arr)
    endtime = time.perf_counter_ns()
    return endtime - starttime  # Time in nanoseconds

if __name__ == "__main__":
    sizes = [100, 300, 500, 700, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]

    print("Benchmarking Insertion Sort:")
    for size in sizes:
        arr = list(range(size, 0, -1))  # Reverse sorted array
        time_taken_ns = time_taken(insertion_sort, arr)
        print(f"Insertion sort on array of size {size}: {time_taken_ns} nanoseconds")
