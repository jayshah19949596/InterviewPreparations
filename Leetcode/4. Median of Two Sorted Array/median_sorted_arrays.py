# Time Complexity is: O(Log(x) + Log(y))

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        half_len = (x + y + 1) // 2

        while low <= high:
            partition_x = (low + high) // 2
            partition_y = half_len - partition_x

            if partition_x == 0: max_left_x = -float("inf")
            else: max_left_x = nums1[partition_x - 1]

            if partition_x == x: min_right_x = float("inf")
            else: min_right_x = nums1[partition_x]

            if partition_y == 0: max_left_y = -float("inf")
            else: max_left_y = nums2[partition_y - 1]

            if partition_y == y: min_right_y = float("inf")
            else: min_right_y = nums2[partition_y]

            # =======================================
            result = max(max_left_x, max_left_y)
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (x + y) % 2 == 0: return (result + min(min_right_x, min_right_y)) / 2
                else: return result
            elif max_left_x > min_right_y: high = partition_x - 1
            else: low = partition_x + 1
