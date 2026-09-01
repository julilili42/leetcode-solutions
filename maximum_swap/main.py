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
METHOD = "maximumSwap"


class Solution:
    def maximumSwap(self, num: int) -> int:
        occurences = [0] * 10
        numbers = list(str(num))

        for i, ch in enumerate(numbers):
            idx = ord(ch) - ord("0")
            occurences[idx] = i

        for i, ch in enumerate(numbers):
            for j in range(len(occurences) - 1, -1, -1):
                if occurences[j] > i and j > int(ch):
                    numbers[i], numbers[occurences[j]] = str(j), numbers[i]
                    return int("".join(numbers))

        return int("".join(numbers))


TESTS = [
    ((2736,), 7236),
    ((9973,), 9973),
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
