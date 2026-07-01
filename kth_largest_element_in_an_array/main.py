from __future__ import annotations

from typing import *
from collections import defaultdict, Counter, deque
from functools import lru_cache, cache
from itertools import accumulate
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
from math import inf, gcd
from random import randint
import sys




# Change this to the LeetCode method name
METHOD = "findKthLargestMinHeap"


# heap is not completely sorted
# in Python: Min-heap is standard
# Min-heap: Binary Tree with constraint:
# each parent is smaller or equal to its children.
#
# For example: [2, 5, 3, 9, 8, 7]
#
#        2
#      /   \
#     5     3
#    / \   /
#   9   8 7
#
# Therfore smallest element is always heap[0]

class Solution:
    # Time: O(n*log(k))
    # Space: O(k)
    def findKthLargestMinHeap(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            # O(log(k))
            heappush(heap, n)
            
            # pop smallest elements from min-heap if min-heap has more than k elements
            # we pop smallest element => Keep all k largest elements
            if len(heap) > k:
                heappop(heap)

        # return smallest element of heap with size k => k-th largest element
        return heap[0]
    
    # Time: O(n + k * log(n))
    # Space: O(n)
    def findKthLargestMaxHeap(self, nums: List[int], k: int) -> int:
        # O(n)
        heap = [-n for n in nums]
        heapify(heap)
        
        # O(k)
        for i in range(k):
            # O(log(n))
            current = heappop(heap)
            if i == k - 1:
                return -current
        
    # Linear Operation O(r - l + 1)
    def partition(self, nums: List[int], l: int, r: int) -> int:
        # choose random pivot
        pivot_index = randint(l, r)
        nums[r], nums[pivot_index] = nums[pivot_index], nums[r]

        i = l

        for j in range(l, r): 
            # compare currrent nums[j] with radom pivot
            if nums[j] <= nums[r]:
                # swap if smaller s.t. all values left of nums[i] are smaller than nums[i]
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        # since all values left of nums[i] are smaller then value at pivot index
        # we found correct position at i
        nums[r], nums[i] = nums[i], nums[r]
        return i

    # Average: O(n)
    # Discards on average half of the array => n, n/2, n/4 ... => O(2n) = O(n)

    # Worst-Case: O(n^2) => If we only discard 1 element at each partition
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # index at which k-th largest element is placed in sorted array
        target = len(nums) - k
        
        l = 0
        r = len(nums) - 1
        # we search for the element which would be located at index target
        while l <= r:
            index = self.partition(nums, l, r)
            if index == target:
            # used element in partition that would be at index target in sorted array
                return nums[index]
            elif index < target:
            # index of used element is to small
            # index + 1, index + 2, etc. have all larger elements
            # search right of current index to find correct element
                l = index + 1
            else:
                r = index - 1




        

        

    

TESTS = [
    (([3,2,1,5,6,4],2), 5),
    (([3,2,3,1,2,4,5,5,6], 4), 4),
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
