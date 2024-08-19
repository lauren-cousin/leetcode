# Given an integer n, return the number of trailing zeroes in n!.
#
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
#
# Example 1:
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
#
# Example 2:
# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
#
# Example 3:
# Input: n = 0
# Output: 0
#
#
# Constraints:
# 0 <= n <= 104
#
# Difficulty: Medium
# Tags: Math
# Time: O(log₅(n)) – The algorithm repeatedly divides n by 5, which gives a logarithmic time complexity base 5.
# Space: O(1) – The algorithm uses a constant amount of extra space, with no additional data structures required.
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 0:
            return -1

        output = 0
        while n >= 5:
            n //= 5
            output += n
        return output