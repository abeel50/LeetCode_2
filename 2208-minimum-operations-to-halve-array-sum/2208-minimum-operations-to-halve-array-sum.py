class Solution:
    def halveArray(self, nums: List[int]) -> int:
      initialSum = 0
      heap = []
      heapify(heap)
      for n in nums:
        heappush(heap, -1 * n)
        initialSum += n

      res = 0
      reducedSum = initialSum
      while reducedSum > initialSum / 2:
        n = (-1 * heappop(heap)) / 2
        reducedSum -= n
        heappush(heap, -1 * n)
        res += 1
      return res