# Description: Return true if the value of the root is equal to the sum of the values of its two children,
# or false otherwise.
# Tags: Tree, Binary Tree
# Time: O(1)
# Space: O(1)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == root.left.val + root.right.val:
            return True
        else:
            return False
