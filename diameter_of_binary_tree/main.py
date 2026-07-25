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
    # Time O(n)
    # Space O(n)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            # need to edit the res value declared outside of dfs
            nonlocal res
            # maximize path length l + r at the current node
            res = max(res, l + r)

            # return depth of subtree rooted at current node
            return 1 + max(l, r)

        dfs(root)
        return res


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
