#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/21 0:27
LeetCode原题链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
"""


class CQueue:
    """设计思想：两个栈，栈是先进后出的结构，要实现队列的先进先出，那么需要这么做：
    一个栈 left 专门作为入列，然后把栈 left 转移到栈 right，将栈 right 作为出列，即可实现队列
    需要考虑：当栈 right 为空时，需要从栈 left 转移，如果栈 left 也为空，返回 -1，
    否则返回 栈 right 的最后一个元素
    """

    def __init__(self):
        self.left_stack = []
        self.right_stack = []

    def appendTail(self, value: int) -> None:
        self.left_stack.append(value)

    def deleteHead(self) -> int:
        while not self.right_stack:
            # 左右栈均为空时，返回 -1
            if not self.left_stack:
                return -1
            while self.left_stack:
                self.right_stack.append(self.left_stack.pop())
        return self.right_stack.pop()


if __name__ == "__main__":
    actual = []
    obj = CQueue()
    actual.append(None)
    actual.append(obj.appendTail(3))
    actual.append(obj.deleteHead())
    actual.append(obj.deleteHead())
    print(f"预期：[None, None, 3, -1]")
    print(f"实际：{actual}")
