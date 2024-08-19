# Given an array nums of length n, return an array answer of length n - 1 such that answer[i] = nums[i] | nums[i + 1] where | is the bitwise OR operation.
#
# Example 1:
# Input: nums = [1,3,7,15]
# Output: [3,7,15]
#
# Example 2:
# Input: nums = [8,4,2]
# Output: [12,6]
#
# Example 3:
# Input: nums = [5,4,9,11]
# Output: [5,13,11]
#
# Constraints:
# 2 <= nums.length <= 100
# 0 <= nums[i] <= 100
#
# Difficulty: Easy
# Tags: Array, Bit Manipulation
# Time: O(n) – because the function iterates through the list nums exactly once, where n is the length of nums.
# Space: O(n) – because the function creates a new list of length n - 1 to store the results.
# Note: Solution uses pairwise, which is available in >= python 3.10 (which has itertools.pairwise available).
class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        return [a | b for a, b in pairwise(nums)]