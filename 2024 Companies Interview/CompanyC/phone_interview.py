"""
You are given an array of integers. Write an algorithm that brings all nonzero elements
to the left of the array, and returns the number of nonzero elements.

[1, 0, 2, 0, 0, 3, 4]   =>   [1, 2, 3, 4, ?, ?, ?], 4 non-zero elements
"""

def find_no_of_nonzero_elem(array):
    if array is not None:
        return -1
    i, j = 0, 0

    while j < len(array):
        if arr[j] != 0:
            arr[i] = arr[j]
            i, j = i + 1, j + 1
        else:
            j += 1
    return i


'''

The CrackCook company store sells stickers that say the word “CrackCook” on them. We just got a new shipment in, and we have way more than we know what to do with. We came up with a plan: we can make posters by cutting and pasting the letters in the word "facebook" to make other words.
Given a particular source string representing a word on a sticker, write a function that tells me how many stickers of that string I need in order to make a given target string. Your function should take in both a source string and target string, and return the number of stickers.

Examples
return ---> -1 source it can be nothing 

source == "crackcook", target == "crr": return 2
source == "crackcook", target == "coo": return 1
source == "crackcook", target == "cookrook": return 2
'''

from collections import Counter


def sticker_used(source, target):
    source_count = Counter(source)
    target_count = Counter(target)
    total_stickers_used = 0
    for char in target_count:
        if char in source_count:
            if target_count[char]>=source_count[char]:
                sticker_used_for_char = target_count[char]//source_count[char]
            else:
                sticker_used_for_char = target_count[char]
            total_stickers_used = max(total_stickers_used, sticker_used_for_char)
        else:
            return -1
    return total_stickers_used

input_list = [["crackcook", "crr"], ["crackcook", "coo"], ["crackcook", "cookrook"], ["crackcook", "fook"]]
for input_ele in input_list:
    answer = sticker_used(input_ele[0], input_ele[1])
    print("input_ele =", input_ele, "output =", answer)
