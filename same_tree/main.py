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
METHOD = "isSameTree"


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base cases
        # if both nodes are none
        if not p and not q:
            return True
        # if one node is none and the other not
        if (not p and q) or (p and not q):
            return False
        # if values are not equal
        if p.val != q.val:
            return False

        # get return values of subtrees
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        # tree is the same if both subtrees are the same
        return left and right


TESTS = [
    # Format:
    # ((arg1, arg2, ...), expected),
    # Example:
    # (([2, 7, 11, 15], 9), [0, 1]),
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
