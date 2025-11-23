import random
import time
import sys
import copy

# Increase recursion depth for deep recursions in deterministic select
sys.setrecursionlimit(10000)

# --- 1. Randomized Quickselect ---

def partition(arr, low, high):
    """
    Standard partition using the last element as pivot.
    Returns the index of the pivot after partitioning.
    """
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def random_partition(arr, low, high):
    """
    Picks a random pivot, swaps with end, and partitions.
    """
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
    return partition(arr, low, high)

def randomized_select(arr, low, high, k):
    """
    Returns the k-th smallest element (0-indexed k) in arr[low..high].
    Expected Time: O(n)
    """
    if low == high:
        return arr[low]

    pivot_index = random_partition(arr, low, high)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return randomized_select(arr, low, pivot_index - 1, k)
    else:
        return randomized_select(arr, pivot_index + 1, high, k)

# --- 2. Deterministic Selection (Median of Medians) ---

def median_of_medians(arr, low, high, k):
    """
    Returns the k-th smallest element using deterministic pivot selection.
    Worst Case Time: O(n)
    """
    if high - low + 1 <= 5:
        # Base case: for small lists, just sort and return
        return sorted(arr[low:high+1])[k - low]

    # 1. Divide arr into groups of 5 and find median of each group
    medians = []
    for i in range(low, high + 1, 5):
        group = arr[i: min(i + 5, high + 1)]
        group.sort()
        medians.append(group[len(group) // 2])

    # 2. Recursively find the median of the medians
    # The median of medians will be at index len(medians)//2 in the medians list
    mom = median_of_medians(medians, 0, len(medians) - 1, len(medians) // 2)

    # 3. Partition around the median of medians
    # First, find mom in current array and swap to end to use standard partition
    # Note: In a strict implementation, we'd modify partition to take value,
    # but searching is O(n) so it doesn't hurt complexity.
    for i in range(low, high + 1):
        if arr[i] == mom:
            arr[i], arr[high] = arr[high], arr[i]
            break
    
    pivot_index = partition(arr, low, high)

    # 4. Recurse
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return median_of_medians(arr, low, pivot_index - 1, k)
    else:
        return median_of_medians(arr, pivot_index + 1, high, k)

# --- Empirical Analysis ---

def run_test():
    n = 5000
    k = n // 2 # Find the median

    print(f"--- Comparison of Selection Algorithms (n={n}, k={k}) ---")

    datasets = {
        "Random": [random.randint(0, 100000) for _ in range(n)],
        "Sorted": list(range(n)),
        "Reverse": list(range(n, 0, -1))
    }

    for name, data in datasets.items():
        print(f"\nDataset: {name}")
        
        # Test Randomized
        arr_copy = data[:]
        start = time.time()
        res = randomized_select(arr_copy, 0, len(arr_copy)-1, k)
        end = time.time()
        print(f"  Randomized Select: Time={end-start:.6f}s, Result={res}")

        # Test Deterministic
        arr_copy = data[:]
        start = time.time()
        res = median_of_medians(arr_copy, 0, len(arr_copy)-1, k)
        end = time.time()
        print(f"  Deterministic Select: Time={end-start:.6f}s, Result={res}")

if __name__ == "__main__":
    run_test()
