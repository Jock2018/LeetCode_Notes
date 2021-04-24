#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/24 11:02
LeetCode原题链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/
"""


class Node:
    """Definition for a Node."""

    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """解法一：利用哈希表存"""

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return

        dic = {}
        cur = head
        # 先存入散列表
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next

        # 再构建节点的 next 和 random 指向
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]


if __name__ == "__main__":
    # 输入：head = [[1, 1], [2, 1]]
    # 输出：[[1, 1], [2, 1]]
    head = Node(1)
    node1 = Node(2)
    head.next = node1
    head.random = node1
    node1.next = None
    node1.random = node1
    solution = Solution()
    print(f"预期：1")
    print(f"实际：{solution.copyRandomList(head).val}")
    print(f"预期：1")
    print(f"实际：{solution.copyRandomList(head).random.val}")
    print(f"预期：2")
    print(f"实际：{solution.copyRandomList(head).next.val}")
    print(f"预期：2")
    print(f"实际：{solution.copyRandomList(head).next.random.val}")
