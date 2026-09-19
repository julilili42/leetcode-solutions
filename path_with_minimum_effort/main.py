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
METHOD = "minimumEffortPath"


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        efforts = [[float("inf")] * n for _ in range(m)]
        efforts[0][0] = 0
        heap = [(0, 0, 0)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while heap:
            effort, i, j = heappop(heap)

            if i == m - 1 and j == n - 1:
                return effort

            if effort > efforts[i][j]:
                continue

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue

                edge_weight = abs(heights[i][j] - heights[ni][nj])

                new_effort = max(effort, edge_weight)

                if new_effort < efforts[ni][nj]:
                    efforts[ni][nj] = new_effort
                    heappush(heap, (new_effort, ni, nj))

        return 0

    def minimumEffortPathDFS(self, heights: list[list[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        res = float("inf")
        visited = set()

        def dfs(i: int, j: int, effort: int):
            if i == m - 1 and j == n - 1:
                nonlocal res
                res = min(res, effort)
                return
            if effort > res:
                return
            if (i, j) in visited:
                return

            visited.add((i, j))
            directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
            for dx, dy in directions:
                if i + dy < 0 or i + dy >= m or j + dx < 0 or j + dx >= n:
                    continue
                cur = abs(heights[i][j] - heights[i + dy][j + dx])
                dfs(i + dy, j + dx, max(cur, effort))

            visited.remove((i, j))

        dfs(0, 0, 0)

        return res


TESTS = [
    (([[1, 2, 2], [3, 8, 2], [5, 3, 5]]), 2),
    (([[1, 2, 3], [3, 8, 4], [5, 3, 5]]), 1),
    (
        (
            [
                [1, 2, 1, 1, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 1, 1, 2, 1],
            ]
        ),
        0,
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
