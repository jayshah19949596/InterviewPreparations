# Explanation
# Because xi < xj,
# yi + yj + |xi - xj| = (yi - xi) + (yj + xj)

# So for each pair of (xj, yj),
# we have xj + yj, and we only need to find out the maximum yi - xi.
# To find out the maximum element in a sliding window,
# we can use priority queue or stack.

# |xi - xj| <= k
# xj-xi <= k
# xj-k <= xi

# https://leetcode.com/problems/max-value-of-equation/discuss/709364/Python3-heap
# https://leetcode.com/problems/max-value-of-equation/discuss/709231/JavaPython-Priority-Queue-and-Deque-Solution-O(N)
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue = []
        result = -float('inf')

        #

        for x, y in points:

            while queue and queue[0][1] < x - k:
                heapq.heappop(queue)
            if queue: result = max(result, -queue[0][0] + y + x)
            heapq.heappush(queue, (x - y, x))

        return result
