#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/9/13 8:33
LeetCode原题链接：https://leetcode-cn.com/problems/path-sum/
"""
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """解法一： 递归"""

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        remain = targetSum - root.val
        return self.hasPathSum(root.left, remain) or self.hasPathSum(root.right, remain)


# class Solution:
#     """解法二： BFS"""
#
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if root is None:
#             return False
#         node_deque = collections.deque([root])
#         value_deque = collections.deque([root.val])
#         while node_deque:
#             now = node_deque.popleft()
#             temp = value_deque.popleft()
#             if now.left is None and now.right is None:
#                 if temp == targetSum:
#                     return True
#                 continue
#             if now.left:
#                 node_deque.append(now.left)
#                 value_deque.append(now.left.val + temp)
#             if now.right:
#                 node_deque.append(now.right)
#                 value_deque.append(now.right.val + temp)
#         return False

# if __name__ == "__main__":
#     solution = Solution()
