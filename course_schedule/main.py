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
METHOD = "canFinish"


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pre = defaultdict(list)

        for course, p in prerequisites:
            pre[course].append(p)

        taken = set()

        def dfs(course):
            if not pre[course]:
                return True

            if course in taken:
                return False

            taken.add(course)
            for p in pre[course]:
                if not dfs(p):
                    return False

            pre[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


TESTS = [
    ((2, [[1, 0]]), True),
    ((2, [[1, 0], [0, 1]]), False),
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
