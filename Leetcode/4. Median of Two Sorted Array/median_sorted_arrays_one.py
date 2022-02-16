# https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
# Merge the sorted array till ((len(nums1)+len(nums2))//2)+1

class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        cur_nums1_ele, cur_nums2_ele = -1, -1
        for count in range(((n + m) // 2) + 1):
            cur_nums2_ele = cur_nums1_ele
            if i != n and j != m:
                if nums1[i] > nums2[j]: cur_nums2_ele, j = nums2[j], j+1
                else: cur_nums1_ele, i = nums1[i], i+1
            elif i < n: cur_nums1_ele, i = nums1[i], i+1
            # for case when j<m,
            else: cur_nums1_ele, j = nums2[j], j+1
        if ((n + m) % 2) == 0: return (cur_nums1_ele + cur_nums2_ele) / 2
        else: return cur_nums1_ele
