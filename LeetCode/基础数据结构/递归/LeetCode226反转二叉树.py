#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/9/13 8:15
LeetCode原题链接：https://leetcode-cn.com/problems/invert-binary-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """递归"""

    def invertTree(self, root: TreeNode) -> [None, TreeNode]:
        if root is None:
            return None
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root


# class Solution:
#     """BFS"""
#
#     def invertTree(self, root: TreeNode) -> [None, TreeNode]:
#         if root is None:
#             return None
#         queue = [root]
#         while queue:
#             tmp = queue.pop()
#             tmp.right, tmp.left = tmp.left, tmp.right
#             if tmp.right:
#                 queue.append(tmp.right)
#             if tmp.left:
#                 queue.append(tmp.left)
#         return root


# if __name__ == "__main__":
#     solution = Solution()
