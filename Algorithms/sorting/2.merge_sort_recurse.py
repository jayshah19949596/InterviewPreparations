"""
Reference Image: https://www.geeksforgeeks.org/merge-sort/
Time: O(N*log(N))
Space: O(N)
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Function to merge two sub-arrays in sorted order.
        def merge(left: int, mid: int, right: int):
            current_left, current_right = left, mid+1
            results = []
            while current_left <= mid and current_right <= right:
                if nums[current_left]<=nums[current_right]:
                    results.append(nums[current_left])
                    current_left += 1
                elif nums[current_left] > nums[current_right]:
                    results.append(nums[current_right])
                    current_right += 1
            while current_left <= mid:
                results.append(nums[current_left])
                current_left += 1
            while current_right <= right:
                results.append(nums[current_right])
                current_right += 1
            nums[left:right+1] = results

        # Recursive function to sort an array using merge sort
        def merge_sort(left: int, right: int):
            if left >= right:
                return
            mid = (left + right) // 2
            # Sort first and second halves recursively.
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            # Merge the sorted halves.
            merge(left, mid, right)

        merge_sort(0, len(nums) - 1)
        return nums