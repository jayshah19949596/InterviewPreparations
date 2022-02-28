# we need to do those tasks with bigger minimum-actual first.
# This is because the bigger minimum-actual, the more energy we save for the next task.
# So we always want to run those tasks which save us more energy which we can use for later tasks.
# Sort the array in the descending order of (minimum - actual).
# (minimum - actual) is the amount of energy that remains after
# finishing a task. So we should try to accumulate as much energy
# as possible in the beginning to complete the tasks coming up
# ahead. Hence, sort the array in descending order based on the
# amount of energy that will be remaining.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda tasks: tasks[1] - tasks[0], reverse=True)
        min_req_energy = cur_energy = 0

        for actual_energy, minimum_energy in tasks:
            if cur_energy < minimum_energy:
                borrow_energy = minimum_energy - cur_energy
                cur_energy += borrow_energy
                min_req_energy += borrow_energy
            cur_energy -= actual_energy

        return min_req_energy
