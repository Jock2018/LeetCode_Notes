#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/20 23:49
LeetCode原题链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
"""

# Definition for singly-linked list.
from typing import List


class ListNode:
    """定义链表"""

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """通过遍历将值存储，再翻转列表即可"""

    def reversePrint(self, head: ListNode) -> List[int]:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result[::-1]


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1)
    middle = ListNode(3)
    tail = ListNode(2)
    head.next = middle
    middle.next = tail
    # head = [1, 3, 2]
    print(f"预期：[2, 3, 1]")
    print(f"实际：{solution.reversePrint(head)}")
