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
METHOD = "orangesRotting"


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        n = len(grid)
        m = len(grid[0])
        res = -1

        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while q:
            res += 1

            for _ in range(len(q)):
                i, j = q.popleft()

                if i + 1 < n and grid[i + 1][j] == 1:
                    q.append([i + 1, j])
                    grid[i + 1][j] = 2
                    fresh -= 1
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    q.append([i - 1, j])
                    grid[i - 1][j] = 2
                    fresh -= 1
                if j + 1 < m and grid[i][j + 1] == 1:
                    q.append([i, j + 1])
                    grid[i][j + 1] = 2
                    fresh -= 1
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    q.append([i, j - 1])
                    grid[i][j - 1] = 2
                    fresh -= 1

        return res if fresh == 0 else -1


TESTS = [
    (([[2, 1, 1], [1, 1, 0], [0, 1, 1]],), 4),
    (([[2, 1, 1], [0, 1, 1], [1, 0, 1]],), -1),
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
