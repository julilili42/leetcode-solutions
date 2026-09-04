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
METHOD = "spiralOrder"


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        res = []

        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = "."

            if (
                not 0 <= x + dx < cols
                or not 0 <= y + dy < rows
                or matrix[y + dy][x + dx] == "."
            ):
                dx, dy = -dy, dx

            x += dx
            y += dy

        return res


# dx, dy = -dy, dx is really nice
# dx = 1
# dy = 0

# dx = 0
# dy = 1

# dx = -1
# dy = 0

# dx = 0
# dy = -1


TESTS = [
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    (
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],),
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
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
