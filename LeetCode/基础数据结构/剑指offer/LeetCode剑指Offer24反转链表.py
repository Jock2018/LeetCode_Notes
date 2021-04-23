#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/22 23:57
LeetCode原题链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    """解题思路：双指针，注意顺序"""

    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


class Solution:
    """解题思路2：递归"""

    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur:
                return pre
            res = recur(cur.next, cur)
            cur.next = pre
            return res

        return recur(head, None)


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # 输入: 1->2->3->4->5->NULL
    # 输出: 5->4->3->2->1->NULL
    print(f"预期：")
    print(f"实际：{solution.reverseList(head).val}")
