# Day03_QuickSort.py
# Quick Sort Implementation in Python

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Original List:", nums)
    sorted_nums = quick_sort(nums)
    print("Sorted List:", sorted_nums)
