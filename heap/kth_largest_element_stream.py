import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap) # O(n)
        while len(self.minHeap) > k: # O(n - k) 
            heapq.heappop(self.minHeap) # O(log n) -> because height of tree is log n

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # O(log n)
        if len(self.minHeap) > self.k: # O(1)
            heapq.heappop(self.minHeap) # O(log n)
        return self.minHeap[0]
    

# So overall -> O(m * log n)