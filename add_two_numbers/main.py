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
METHOD = "addTwoNumbers"


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = ListNode()
        dummy = res

        carry = 0
        while l1 or l2:
            add = ListNode()
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry

            carry = total // 10
            add.val = total % 10

            res.next = add
            res = res.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry == 1:
            res.next = ListNode(1)

        return dummy.next

    def addTwoNumbersBad(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = ListNode()
        dummy = ListNode()
        dummy = res

        of = 0
        while l1 and l2:
            add = ListNode()
            total = l2.val + l1.val + of
            if total >= 10:
                add.val = total - 10
                of = 1
            else:
                add.val = total
                of = 0

            res.next = add
            res = res.next

            l1 = l1.next
            l2 = l2.next

        if not l1 and not l2 and of == 0:
            return dummy.next

        while l1:
            add = ListNode()
            total = l1.val + of
            if total >= 10:
                add.val = total - 10
                of = 1
            else:
                add.val = total
                of = 0

            res.next = add
            res = res.next

            l1 = l1.next

        while l2:
            add = ListNode()
            total = l2.val + of
            if total >= 10:
                add.val = total - 10
                of = 1
            else:
                add.val = total
                of = 0

            res.next = add
            res = res.next

            l2 = l2.next

        if of == 1:
            add = ListNode(1)
            res.next = add

        return dummy.next


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
