# https://leetcode.com/problems/snapshot-array/
# Implement a SnapshotArray that supports the following interface:

class SnapshotArrayOneAnsBelow:
    def __init__(self, length: int):
        self.arr = [0 for i in range(length)]
        self.snap_map = {}
        self.snap_time = -1

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        self.snap_time += 1
        self.snap_map[self.snap_time] = self.arr[:]
        return self.snap_time

    def get(self, index: int, snap_id: int) -> int:
        return self.snap_map[snap_id][index]