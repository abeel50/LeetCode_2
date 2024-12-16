class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:     
      heap = []
      heapify(heap)
      for i,n in enumerate(nums):
        heappush(heap, (n, i))

      while k > 0:
        n,i = heappop(heap)
        heappush(heap, (n*multiplier, i))
        nums[i] = n * multiplier
        k -= 1
        
      return nums
        