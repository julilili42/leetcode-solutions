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
METHOD = "generateParenthesis"


class Solution:
    # Time O(R * n) where R is number of valid combinations
    # per valid solution we need 2n recursion levels where each recursion is O(1)
    # Therefore O(R * n)
    # Space O(R * n)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
    
        # add ")" only after valid "("
        def dfs(s: str, left: int, right: int):
            # if we have n opening and n closing parenthesis we are done
            if left == n and right == n:
                res.append(s)
                return
            
            if left < n:
                dfs(s + "(", left + 1, right)
            
            # right has to be smaller then left, else we enter a invalid branch
            if right < left:
                dfs(s + ")", left, right + 1)
        

        dfs("", 0, 0)
            
        return res


TESTS = [
    ((3,), ["((()))","(()())","(())()","()(())","()()()"]),
    ((1,), ["()"]),
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
