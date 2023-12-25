def partition(arr, low, high):
    i = low - 1  # index of smaller element
    pivot_idx = high
    pivot_element = array[pivot_idx]  # pivot element
    for j in range(low, high):
        if arr[j] <= pivot_element:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    array[i + 1], array[pivot_idx] = array[pivot_idx], array[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low <= high:
        pivot_index = partition(arr, low, high)

        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            return quickselect(arr, pivot_index + 1, high, k)
        else:
            return quickselect(arr, low, pivot_index - 1, k)

def find_kth_largest(arr, k):
    n = len(arr)
    if k > 0 and k <= n:
        # kth largest element is at index n - k
        return quickselect(arr, 0, n - 1, n - k)
    else:
        return "Invalid value of k"

# Example usage
arr = [50, 5, 6, 9, 2, 2, 10, 1, 52]
k = 3
result = find_kth_largest(arr, k)
print(f"The {k}-th largest element is: {result} and array has changed to: {arr}")