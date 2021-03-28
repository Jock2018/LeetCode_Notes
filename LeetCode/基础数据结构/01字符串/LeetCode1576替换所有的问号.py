#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/3/28 21:43
LeetCode原题链接：https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
"""


class Solution:
    """解法一：遍历 + 特殊处理

    简单题，遍历一遍字符串，遇到 "?" 用前后不同的字符替代。注意边界处理：
    1. "a??b" 的情况，"?" 后面跟着 "?" 时,只考虑不和前面字母相同即可。
    2. "?abc" 的情况，"?" 放在最开始时，只考虑不和后面相同即可。
    3. "a?b" 的情况，"?" 放在中间，需要考虑前后都不相同。
    4. "a?" 的情况，"?" 放在最后，只考虑不和前面字符相同即可。
    5. "??" 的情况，情况同上
    6. "?" 的情况，赋值为 ”a" 返回即可
    """

    def modifyString(self, s: str) -> str:
        alpha_list = list(s)

        # 处理长度为 1 的情况
        if len(s) == 1:
            if s != "?":
                return s
            return "a"

        # 处理长度 > 1 且第一个为 "?" 的情况
        if alpha_list[0] == "?":
            for j in range(97, 123):
                if j != ord(alpha_list[1]):
                    alpha_list[0] = chr(j)
                    break
        # 处理长度 > 1 且最后一个为 "?" 的情况
        if alpha_list[-1] == "?":
            for i in range(122, 97, -1):
                if i != ord(alpha_list[-2]):
                    alpha_list[-1] = chr(i)
                    break
        # 处理中间字符
        for i in range(1, len(s) - 1):
            if alpha_list[i] == "?":
                for j in range(97, 123):
                    if j not in (ord(alpha_list[i - 1]), ord(alpha_list[i + 1])):
                        alpha_list[i] = chr(j)
                        break
        return "".join(alpha_list)


class Solution2:
    """解法二：遍历 + 引入虚节点

    该解法参考了 sunrise 的题解：https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/solution/onzhi-zhen-cha-zhao-by-sunrise-z/
    引入虚节点，可以避免特判，从而简化代码处理逻辑，很巧妙。
    解法一需要单独处理第一和最后为 "?" 的情况。
    所以我们在字符串前后引入特殊字符，如 "*" 即可避免特殊处理了。

    代码处理逻辑：出现 ? 时，从 a-z 找到与 ? 前后字符都不同的第一个字符，然后进行替换。
    """

    def modifyString(self, s: str) -> str:
        # 构造 a-z 备选字母
        replace_alphas = "".join(chr(i) for i in range(97, 123))

        # 首尾添加特殊字符，作为虚节点
        result = list(f"*{s}*")

        for i in range(1, len(result) - 1):
            if result[i] == "?":
                for alpha in replace_alphas:
                    if alpha not in (result[i - 1], result[i + 1]):
                        result[i] = alpha
                        break
        return "".join(result[1:-1])


if __name__ == "__main__":
    solution = Solution()
    string = "ubv?w"
    print(f"预期：ubvaw")
    print(f"实际：{solution.modifyString(string)}")

    solution = Solution()
    string = "??yw?ipkj?"
    print(f"预期：abywaipkjz")
    print(f"实际：{solution.modifyString(string)}")

    solution = Solution2()
    string = "ubv?w"
    print(f"预期：ubvaw")
    print(f"实际：{solution.modifyString(string)}")

    solution = Solution2()
    string = "??yw?ipkj?"
    print(f"预期：abywaipkja")
    print(f"实际：{solution.modifyString(string)}")
