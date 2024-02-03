"""
Given a binary tree, imagine yourself standing on the left side of it, return the values of the nodes you can see ordered from bottom to top, then switch to right side of the tree, and return the values of the nodes you can see ordered from top to bottom.

For example, given:
Binary Tree:
--->      1.  0
         / \.
--->    2   3   <--- 1
       / \ /
--->   6 5 4    <---  2

Answer: [6, 2, 1, 3, 4]

--->       1
         /   \
--->    2     3    <---
         \
--->      5        <---

Answer: [5, 2, 1, 3, 5]

"""


class Node:
    def __init__(self, left, right, val):
        self.val = val
        self.left = left
        self.right = right

def tree_traversal(root):
    traversal_list = []
    cur_level = [root]
    max_level = 0
    level_map = defaultdict(list)
    level_map[0] = cur_level[:]
    while cur_level:
        next_level = []
        for node in cur_level:
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)

        max_level += 1
        level_map[max_level] = [next_level[0], next_level[-1]]
        cur_level = next_level

    level_number = max_level - 1
    while level_number >= 0:
        traversal_list.append(level_map[level_number][0].val)
        level_number -= 1

    level_number = 1
    while level_number < max_level:
        traversal_list.append(level_map[level_number][-1].val)
        level_number += 1

    return traversal_list

"""
Implement a mock of cd (change directory) command on Unix. The code doesn't have to change actual directories, just return the new path after cd was executed.
 
The function takes two arguments (current working directory and directory to change to), and returns the output directory as if cd command was executed. There's no filesystem underneath; all paths are valid.
 
Example table of inputs and outputs:
| cwd      | cd (arg)       | output
| -------- | -------------- | ------
| /        | foo            | /foo
| /baz     | /bar           | /bar
| /foo/bar | ../../../../.. | /
| /x/y     | ../p/../q      | /x/q
| /x/y     | /p/./q         | /p/q 
"""

def mock_cd(cwd, argument):
    argument_list = argument.split("/")

    if argument[0] == "/":
        output_dir = []
    else:
        output_dir = cwd.split("/")

    for element in argument_list:
        if element == ".."
            if output_dir:
                output_dir.pop()
        elif element == ".":
            continue
        else:
            output_dir.append(element)

    return "/" +"/".join(output_dir)
