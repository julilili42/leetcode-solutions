from __future__ import annotations

from typing import *
from collections import defaultdict, Counter, deque
from functools import lru_cache, cache
from itertools import accumulate
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
from math import inf, gcd
import sys


# Change this to the LeetCode method name
METHOD = "multiply"


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)

        res = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                # mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                # if not int allowed
                sum_ = mul + res[i + j + 1]
                res[i + j + 1] = sum_ % 10
                res[i + j] += sum_ // 10

        product = "".join(map(str, res)).lstrip("0")
        return product if product else "0"


TESTS = [
    (("2", "3"), "6"),
    (("123", "456"), "56088"),
]


def run_tests():
    solution = Solution()
    fn = getattr(solution, METHOD)

    if not TESTS:
        print("No tests yet.")
        return

    for i, (args, expected) in enumerate(TESTS, 1):
        got = fn(*args)

        if got == expected:
            print(f"Test {i}: OK")
        else:
            print(f"Test {i}: FAIL")
            print(f"  got:      {got}")
            print(f"  expected: {expected}")


if __name__ == "__main__":
    run_tests()
