"""
You live in San Francisco city and want to minimize your commute time to the Amazon HQ.

Given a 2D matrix of the Seattl grid and the time as well as cost matrix of all the available transportation
modes, return the fastest mode of transportation. If there are multiple such modes then return one with the least cost.

Rules:
1. The input grid represents the city blocks, so the commuter is only allowed to travel along the horizontal and vertical axes.
Diagonal traversal is not permitted.
2. The commuter can only move to the neighboring cells with the same transportation mode.

Sample Input:

2D Grid:              Legend:
|3|3|S|2|X|X|         X = Roadblock
|3|1|1|2|X|2|         S = Source
|3|1|1|2|2|2|         D = Destination
|3|1|1|1|D|3|         1 = Walk, 2 = Bike, 3 = Car, 4 = Train
|3|3|3|3|3|4|
|4|4|4|4|4|4|

Transportation Modes:        ["Walk", "Bike", "Car", "Train"]
Cost Matrix (Dollars/Block): [0,      1,      3,     2]
Time Matrix (Minutes/Block): [3,      2,      1,     1]

0. 1 2 3 4 5
|3|3|S|2|X|X| 0         X = Roadblock
|3|1|1|2|X|2| 1        S = Source
|3|1|1|2|2|2| 2        D = Destination
|3|1|1|1|D|3| 3        1 = Walk, 2 = Bike, 3 = Car, 4 = Train
|3|3|3|3|3|4| 4
|4|4|4|4|4|4| 5

walk = 3*4 cells = 12, 0
bike = 2*4 cells =  8, 1*3 = 1
car = 10*1 = 10,
"""
from collections import deque
from collections import defaultdict


def find_start_end(mat):
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] == "S":
                start = (r, c)
            if mat[r][c] == "D":
                end = (r, c)

    return start, end


def get_neightbors(cur_row, cur_col, n, m):
    neighbor_rows = [1, 0, -1, 0]
    neighbor_cols = [0, 1, 0, -1]
    neighbors = []
    for nr, nc in zip(neighbor_rows, neighbor_cols):
        new_row = nr + cur_row
        new_col = nc + cur_col
        if 0 <= new_row < n and 0 <= new_col < m:
            neighbors.append([nr + cur_row, nc + cur_col])
    return neighbors


def find_transportation(mat, cost_list, time_list):
    start, end = find_start_end(mat)
    start_val = mat[start[0]][start[1]]
    queue = deque([[[start[0], start[1]], start_val, 0, 0]])
    trans_mode_map = defaultdict(list)
    visited = set([])
    visited.add((start[0], start[1]))

    while queue:
        # print(queue)
        cur_cell, cur_val, cur_time, cur_cost = queue.pop()
        if cur_val == "D":
            if cur_val in trans_mode_map and trans_mode_map[cur_val][0] > cur_time:
                trans_mode_map[cur_val] = [cur_time, cur_cost]
            elif cur_val in trans_mode_map and trans_mode_map[cur_val][0] == cur_time and trans_mode_map[cur_val][
                1] > cur_cost:
                trans_mode_map[cur_val] = [cur_time, cur_cost]
            else:
                trans_mode_map[cur_val] = [cur_time, cur_cost]

        neighbors = get_neightbors(cur_cell[0], cur_cell[1], len(grid), len(grid[0]))
        for nr, nc in neighbors:
            value = mat[nr][nc]
            cost, time = 0, 0
            if value.isdigit():
                cost = cost_list[int(value) - 1]
                time = time_list[int(value) - 1]

            if cur_val in ["S", "D"] and:
                visited.add((nr, nc))
                queue.appendleft([[nr, nc], cur_val, cur_time + time, cur_cost + cost])
            elif value != "X" and cur_val == value and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.appendleft([[nr, nc], cur_val, cur_time + time, cur_cost + cost])

    best_mode, best_time, best_cost = None, float('inf'), float('inf')
    for mode in trans_mode_map:
        time, cost = trans_mode_map[mode]
        if time < best_time:
            best_mode, best_time, best_cost = mode, time, cost
        elif time == best_time and cost < best_cost:
            best_mode, best_time, best_cost = mode, time, cost

    return best_mode


grid = [
    ["3", "3", "S", "2", "X", "X"],
    ["3", "1", "1", "2", "X", "2"],
    ["3", "1", "1", "2", "2", "2"],
    ["3", "1", "1", "1", "D", "3"],
    ["3", "3", "3", "3", "3", "4"],
    ["4", "4", "4", "4", "4", "4"]
]

cost_matrix = [0, 1, 3, 2]

time_matrix = [3, 2, 1, 1]

fastest_mode = find_transportation(grid, cost_matrix, time_matrix)
print("fastest_mode", fastest_mode)
