# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
#
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
#
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
#
# Difficulty: Easy
# Tags: Array, Hash Table, Sorting
# Time Complexity: O(n), because you iterate through the list once, performing O(1) operations for checking and adding elements to the set.
# Space Complexity: O(n), because in the worst case (when all elements are unique), the set needs to store all n elements.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 1
        return False

