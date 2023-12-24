"""
QuickSort is a sorting algorithm based on the Divide and Conquer algorithm.
It picks an element as a pivot and partitions the given array around the picked pivot.
Algo then places the pivot in its correct position in the sorted array.

Reference Image: https://favtutor.com/blogs/quick-sort-cpp

Time Complexity:

Best Case: O(N log (N))
The best-case scenario for quicksort occur when the pivot chosen at each step divides the array into roughly equal halves.
In this case, the algorithm will make balanced partitions, leading to efficient Sorting.

Average Case: O ( N log (N))
Quicksort’s average-case performance is usually very good in practice, making it one of the fastest sorting Algorithm.

Worst Case: O(N^2)
The worst-case Scenario for Quicksort occur when the pivot at each step consistently results in highly unbalanced partitions.
"""


def partition(array, low, high):
    i = low - 1  # index of smaller element
    pivot_idx = high
    pivot_element = array[pivot_idx]  # pivot element
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if array[j] <= pivot_element:
            i += 1  # increment index of smaller element
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[pivot_idx] = array[pivot_idx], array[i + 1]
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)  # pi is partitioning index, arr[p] is now at right place

        # Separately sort elements before partition and after partition
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


nums = [2, 6, 5, 3, 8, 7, 1, 0]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
