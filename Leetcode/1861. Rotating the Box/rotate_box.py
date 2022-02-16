'''
https://leetcode.com/problems/rotating-the-box/
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:
1. A stone '#'
2. A stationary obstacle '*'
3. Empty '.'

The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity.
Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box.
Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.
It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.
Return an n x m matrix representing the box after the rotation described above.

Time : O(R*C)
Space: O(R*C)
'''


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        # horizontal sliding window with  "write_col" as write head
        for row in range(rows):
            write_col = cols - 1
            for col in range(cols - 1, -1, -1):
                if box[row][col] == '*':
                    write_col = col - 1
                elif box[row][col] == '#':
                    box[row][col], box[row][write_col] = box[row][write_col], box[row][col]
                    write_col -= 1

        return zip(*box[:: -1])  # Rotate the box
