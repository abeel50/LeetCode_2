class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
      heap = []
      heapify(heap)
      for n in nums:
        heappush(heap, -1 * n)

      res = 0
      for i in range(k):
        n = -1 * heappop(heap)
        res += n
        heappush(heap, -1 * ceil(n/3))
      return res