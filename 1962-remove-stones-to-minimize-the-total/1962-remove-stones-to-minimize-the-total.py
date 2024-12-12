class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
      heap = []
      heapify(heap)
      for p in piles:
        heappush(heap, -1 * p)

      
      for i in range(k):
        p = -1 * heappop(heap)
        heappush(heap, -1 * (p - floor(p / 2)))
      
      return -1 * sum(heap)