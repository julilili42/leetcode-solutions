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
METHOD = "hasCycle"


class Solution:
    # Time: O(n) 
    # Worstcase cycle with n nodes => in n steps: d mod cycle_length == 0
    # Space: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # we could also check fast.next.next but this would be caught in the next iterration
        # relative distance between both pointers in cycle increases by one each iteration
        # fast: +2 -> +2 -> +2 -> ...
        # slow: +1 -> +1 -> +1 -> ...
        # relative: +1 -> +1 -> +1 -> ...
        # if we are in a cycle relative distance d mod cycle_length
        # and since d incereases by 1 it is guranteed that slow == fast at some point
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False

TESTS = [
    (([3,2,0,-4],), True),
    (([1,2],), True),
    (([1],), False),
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
