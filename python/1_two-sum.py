# Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they
# add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Difficulty: Easy
# Tags: Array, Hash Table

# Brute Force Approach
# Time: O(n^2), where n is the number of elements in nums. For each element, we check every other element.
# Space: O(1), since no extra space is needed beyond the input.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:], start=i+1):
                if num1 + num2 == target:
                    return [i, j]

# Optimal Approach (Hash Table)
# Time: O(n), as we traverse the list containing n elements only once. Each lookup in the table costs only O(1) time.
# Space: O(n), for the extra space used by the seen dictionary.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i