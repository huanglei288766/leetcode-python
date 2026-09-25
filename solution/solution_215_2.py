import heapq
from typing import List

from solution.solution_215_1 import findKthLargest


class Solution:
    def findKthLargest(self, nums, k):
        min_heap = []
        heapq.heapify(min_heap)
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                if num > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)
        return min_heap[0]

def quickSort(nums, start, end):
    if start >= end:
        return


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    findKthLargest(nums, 0, len(nums) - 1, 2)

    print(findKthLargest(nums, 0, len(nums) - 1, 2))






class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return 0;

