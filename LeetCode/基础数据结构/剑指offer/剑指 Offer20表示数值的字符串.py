#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/4/18 21:05
LeetCode原题链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/
"""
from enum import Enum


def is_digit(right):
    if right.startswith("+") or right.startswith("-"):
        right = right[1:]
    return right.isdigit()


class Solution1:
    """解法一：穷举"""

    def isNumber(self, s: str) -> bool:
        s = s.lower().strip()
        if s.startswith("+") or s.startswith("-"):
            s = s[1:]
        if s.count("e") == 1:
            left, right = s.split("e")
            left = left.replace(".", "", 1)
            return left.isdecimal() and is_digit(right)
        s = s.replace(".", "", 1)
        return s.isdecimal()


class Solution2:
    """解法二：官方题解：确定性有穷状态机"""

    def isNumber(self, s: str) -> bool:
        State = Enum("State", [
            "STATE_INITIAL",
            "STATE_INT_SIGN",
            "STATE_INTEGER",
            "STATE_POINT",
            "STATE_POINT_WITHOUT_INT",
            "STATE_FRACTION",
            "STATE_EXP",
            "STATE_EXP_SIGN",
            "STATE_EXP_NUMBER",
            "STATE_END",
        ])
        Chartype = Enum("Chartype", [
            "CHAR_NUMBER",
            "CHAR_EXP",
            "CHAR_POINT",
            "CHAR_SIGN",
            "CHAR_SPACE",
            "CHAR_ILLEGAL",
        ])

        def toChartype(ch: str) -> Chartype:
            if ch.isdigit():
                return Chartype.CHAR_NUMBER
            elif ch.lower() == "e":
                return Chartype.CHAR_EXP
            elif ch == ".":
                return Chartype.CHAR_POINT
            elif ch == "+" or ch == "-":
                return Chartype.CHAR_SIGN
            elif ch == " ":
                return Chartype.CHAR_SPACE
            else:
                return Chartype.CHAR_ILLEGAL

        transfer = {
            State.STATE_INITIAL: {
                Chartype.CHAR_SPACE: State.STATE_INITIAL,
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
                Chartype.CHAR_SIGN: State.STATE_INT_SIGN,
            },
            State.STATE_INT_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
            },
            State.STATE_INTEGER: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_POINT: State.STATE_POINT,
                Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_POINT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_POINT_WITHOUT_INT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
            },
            State.STATE_FRACTION: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_EXP: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                Chartype.CHAR_SIGN: State.STATE_EXP_SIGN,
            },
            State.STATE_EXP_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
            },
            State.STATE_EXP_NUMBER: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_END: {
                Chartype.CHAR_SPACE: State.STATE_END,
            },
        }

        st = State.STATE_INITIAL
        for ch in s:
            typ = toChartype(ch)
            if typ not in transfer[st]:
                return False
            st = transfer[st][typ]

        return st in [State.STATE_INTEGER, State.STATE_POINT, State.STATE_FRACTION, State.STATE_EXP_NUMBER,
                      State.STATE_END]


class Solution:
    """解法三：调 API"""

    def isNumber(self, s: str) -> bool:
        try:
            float(s)
        except Exception:
            return False
        return True


if __name__ == "__main__":
    solution = Solution()
    for s in ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]:
    # for s in ["46.32"]:
        print(f"预期：True")
        print(f"实际：{solution.isNumber(s)}")
    # 例如，字符串 "+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123" 都表示数值，
    # 但 "12e"、"1a3.14"、"1.2.3"、"+-5" 及 "12e+5.4" 都不是
    print("-----------------------------------------")
    for s in ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]:
    # for s in ["+ 1"]:
        print(f"预期：False")
        print(f"实际：{solution.isNumber(s)}")
