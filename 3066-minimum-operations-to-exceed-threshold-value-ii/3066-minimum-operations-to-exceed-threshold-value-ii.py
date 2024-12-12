class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
      heap = []
      kCount = 0
      heapify(heap)
      for n in nums:
        heappush(heap, n)
        if n >= k:
          kCount += 1

      res = 0
      while kCount < len(heap) and len(heap) >= 2:
        x = heappop(heap)
        y = heappop(heap)
        n = (min(x, y) * 2) + max(x, y) 
        if n >= k:
          kCount += 1
        heappush(heap, n)
        res += 1
        
      return res
        