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
METHOD = "minCostConnectPoints"


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        visited = [False] * n
        min_distance = [float("inf")] * n
        min_distance[0] = 0

        res = 0
        for _ in range(n):
            u = -1

            # find next smallest point
            for i in range(n):
                if not visited[i] and (u == -1 or min_distance[i] < min_distance[u]):
                    u = i

            visited[u] = True
            res += min_distance[u]

            for v in range(n):
                if not visited[v]:
                    distance = abs(points[u][0] - points[v][0]) + abs(
                        points[u][1] - points[v][1]
                    )

                    min_distance[v] = min(min_distance[v], distance)

        return res


TESTS = [
    (([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]],), 20),
    (([[3, 12], [-2, 5], [-4, 1]],), 18),
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
