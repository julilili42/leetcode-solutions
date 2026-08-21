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
METHOD = "plusOne"


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        return [1] + digits

    def plusOneRecursive(self, digits: List[int]) -> List[int]:
        res = digits

        def dfs(i: int, of: int):
            nonlocal res
            if i < 0:
                if of == 1:
                    res.insert(0, 1)
                return

            if res[i] + of == 10:
                res[i] = 0
                of = 1
            else:
                res[i] += of
                of = 0

            dfs(i - 1, of)

        dfs(len(digits) - 1, 1)
        return res

    def plusOneNaiv(self, digits: List[int]) -> List[int]:
        temp = ""
        for d in digits:
            temp += str(d)

        number = int(temp)
        number += 1
        number = str(number)

        res = []
        for ch in number:
            res.append(int(ch))

        return res


TESTS = [
    (([1, 2, 3],), [1, 2, 4]),
    (([4, 3, 2, 1],), [4, 3, 2, 2]),
    (([9],), [1, 0]),
    (([1, 2, 9, 9, 9],), [1, 3, 0, 0, 0]),
    (([9, 8, 7, 6, 5, 4, 3, 2, 1, 0],), [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]),
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
