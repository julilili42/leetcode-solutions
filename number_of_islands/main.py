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
METHOD = "numIslands"


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        m = len(grid)
        n = len(grid[0])

        # Time: O(n * m)
        # Space: O(n * m)
        # go through each entry in grid
        # if entry is a 1, start BFS from this entry and change visited entries to 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    res += 1

                    q = deque([[r, c]])
                    grid[r][c] = "0"

                    while q:
                        row, col = q.popleft()
                        # up
                        if row + 1 < m and grid[row + 1][col] == "1":
                            grid[row + 1][col] = "0"
                            q.append([row + 1, col])
                        # down
                        if row - 1 >= 0 and grid[row - 1][col] == "1":
                            grid[row - 1][col] = "0"
                            q.append([row - 1, col])
                        # right
                        if col + 1 < n and grid[row][col + 1] == "1":
                            grid[row][col + 1] = "0"
                            q.append([row, col + 1])
                        # left
                        if col - 1 >= 0 and grid[row][col - 1] == "1":
                            grid[row][col - 1] = "0"
                            q.append([row, col - 1])

        return res


TESTS = [
    (
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
        ),
        1,
    ),
    (
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
        ),
        3,
    ),
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
