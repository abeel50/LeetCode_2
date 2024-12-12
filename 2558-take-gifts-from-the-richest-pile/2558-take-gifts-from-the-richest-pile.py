class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
      heap = []
      heapify(heap)
      for g in gifts:
        heappush(heap, -1 * g)

      
      for i in range(k):
        g = -1 * heappop(heap)
        heappush(heap, -1 * floor(sqrt(g)))
      
      return -1 * sum(heap)