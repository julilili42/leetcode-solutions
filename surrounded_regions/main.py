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
METHOD = "solve"


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}

        # all O cells on the edge must be kept.
        # starting bfs on these cells from the edge therefore leads us
        # to all cells which we should keep.
        q = deque()

        # left and right
        for i in range(m):
            for j in (0, n - 1):
                if board[i][j] == "O":
                    board[i][j] = "#"
                    q.append((i, j))

        # top and bottom
        for i in (0, m - 1):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "#"
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for di, dj in directions:
                if not 0 <= i + di <= m - 1 or not 0 <= j + dj <= n - 1:
                    continue

                if board[i + di][j + dj] == "O":
                    board[i + di][j + dj] = "#"
                    q.append((i + di, j + dj))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"


TESTS = [
    (
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ]
        ),
        [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ],
    ),
    (([["X"]]), [["X"]]),
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
