#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
时间：2021/3/31 23:15
LeetCode原题链接：https://leetcode-cn.com/problems/validate-ip-address/
"""
import re


class Solution:
    """解法一：按照题目意思构造条件 + 分治法"""

    ipv6_pattern = re.compile(r"[0-9a-fA-F]+")

    def validIPAddress(self, IP: str) -> str:
        if self._isIpv4(IP):
            return "IPv4"
        if self._isIpv6(IP):
            return "IPv6"
        return "Neither"

    def _isIpv4(slef, IP):
        ip_segment_list = IP.split(".")
        if len(ip_segment_list) == 4:
            for ip_segment in ip_segment_list:
                if ip_segment.startswith("0") and len(ip_segment) > 1:
                    return False
                if not ip_segment.isdigit():
                    return False
                if int(ip_segment) < 0 or int(ip_segment) > 255:
                    return False
            return True
        return False

    def _isIpv6(self, IP):
        ip_segment_list = IP.split(":")
        if len(ip_segment_list) == 8:
            for ip_segment in ip_segment_list:
                if len(ip_segment) > 4 or len(ip_segment) == 0:
                    return False
                match = self.ipv6_pattern.match(ip_segment)
                if not match or match.group(0) != ip_segment:
                    return False
            return True
        return False


if __name__ == "__main__":
    solution = Solution()
    IP = "172.16.254.1"
    print(f"预期：IPv4")
    print(f"实际：{solution.validIPAddress(IP)}")

    solution = Solution()
    IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    print(f"预期：IPv6")
    print(f"实际：{solution.validIPAddress(IP)}")

    solution = Solution()
    IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
    print(f"预期：Neither")
    print(f"实际：{solution.validIPAddress(IP)}")

    solution = Solution()
    IP = "2001:0db8:85a3:0000:0:8A2E:0370:733a"
    print(f"预期：IPv6")
    print(f"实际：{solution.validIPAddress(IP)}")

    solution = Solution()
    IP = "20EE:FGb8:85a3:0:0:8A2E:0370:7334"
    print(f"预期：Neither")
    print(f"实际：{solution.validIPAddress(IP)}")

    solution = Solution()
    IP = "192.0.0.1"
    print(f"预期：IPv4")
    print(f"实际：{solution.validIPAddress(IP)}")
