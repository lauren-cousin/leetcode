# Description: Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Difficulty: Easy
# Tags: Array, Prefix Sum
# Time: O(n)
# Space: O(1)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

# Time: O(n)
# Space: O(n) -> have to access and store sum, sumList
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         sum = 0
#         sumList = []
#         for num in nums:
#             sum += num
#             sumList.append(sum)
#         return sumList