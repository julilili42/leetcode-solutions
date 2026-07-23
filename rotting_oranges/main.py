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
        m = len(grid)
        n = len(grid[0])
        res = 0
        fresh = 0
        q = deque([])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    fresh += 1
                # must start BFS from each rotten node
                # therefore first add all rotten nodes
                if grid[row][col] == 2:
                    q.append([row, col])

        while q and fresh > 0:
            # since we want level traverse we need the nodes in the q
            # to be from the same level
            for _ in range(len(q)):
                i, j = q.popleft()

                if i + 1 < m and grid[i + 1][j] == 1:
                    q.append([i + 1, j])
                    grid[i + 1][j] = 2
                    fresh -= 1
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    q.append([i - 1, j])
                    grid[i - 1][j] = 2
                    fresh -= 1
                if j + 1 < n and grid[i][j + 1] == 1:
                    q.append([i, j + 1])
                    grid[i][j + 1] = 2
                    fresh -= 1
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    q.append([i, j - 1])
                    grid[i][j - 1] = 2
                    fresh -= 1

            res += 1

        return -1 if fresh > 0 else res


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
