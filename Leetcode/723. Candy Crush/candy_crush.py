'''
https://leetcode.com/problems/candy-crush/submissions/
Design candy crush algorithm.

This question is about implementing a basic elimination algorithm for Candy Crush.

Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy.
A value of board[i][j] == 0 represents that the cell is empty.
The given board represents the state of the game following the player's move.
Now, you need to restore the board to a stable state by crushing candies according to the following rules:
1. If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time -
   these positions become empty.
2. After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these
   candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.
3. After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
4. If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.

Complexity Analysis
    1. Time Complexity: O((R*C)^2)), where R, CR,C is the number of rows and columns in board.
                       We need O(R*C) to scan the board, and we might crush only 3 candies repeatedly.
    2. Space Complexity: O(1) additional complexity, as we edit the board in place.
'''


class Solution(object):
    def candyCrush(self, board):
        rows, cols = len(board), len(board[0])
        todo = False
        # Tracking candies needed to be crushed on same row
        for row in range(rows):
            for col in range(cols-2):
                if abs(board[row][col]) == abs(board[row][col+1]) == abs(board[row][col+2]) != 0:
                    board[row][col] = board[row][col+1] = board[row][col+2] = -abs(board[row][col])
                    todo = True
        # Tracking candies needed to be crushed on same col
        for row in range(rows-2):
            for col in range(cols):
                if abs(board[row][col]) == abs(board[row+1][col]) == abs(board[row+2][col]) != 0:
                    board[row][col] = board[row+1][col] = board[row+2][col] = -abs(board[row][col])
                    todo = True
        # Vertical sliding window where "write_row" is write head
        for col in range(cols):
            write_row = rows-1
            for row in range(rows-1, -1, -1):
                if board[row][col] > 0:
                    board[write_row][col] = board[row][col]
                    write_row -= 1
            for row in range(write_row, -1, -1):  # Filling the other row in the column with 0
                board[row][col] = 0

        return self.candyCrush(board) if todo else board
