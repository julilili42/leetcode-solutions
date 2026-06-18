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
METHOD = "searchMatrix"


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        l = 0
        r = rows * columns - 1

        while l <= r:
            m = l + (r-l) // 2
            # we need to find the correct value in the matrix.
            # first find correct index of list: m // columns
            # second find correct index in found list: m % columns
            # where columns is the length of the arrays
            current = matrix[m // columns][m % columns]

            if current == target:
                return True
            elif current < target:
                l = m + 1
            else:
                r = m - 1

        return False





    # find target or (insert_index - 1)
    def binary_search(self, nums: List[int], target: int, floor: bool = False) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        floor_index = l - 1 if (l - 1) >= 0 else 0
        return floor_index if floor else -1

    # Time O(m + log(m) + log(n))
    def searchMatrixTwoSearches(self, matrix: List[List[int]], target: int) -> bool:
        # O(m) Runtime
        first_column = [l[0] for l in matrix]
        # search first_column to find row to search for target
        index = self.binary_search(first_column, target, True) 
        search_row = matrix[index]
        found_index = self.binary_search(search_row, target) 
        return True if found_index != -1 else False


TESTS = [
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3,), True),
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13,), False),
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
