class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
      nums.sort(reverse = True)
      h = {}
      for n in nums:
        if n * n in h:
          h[n] = h[n*n] + 1
        else:
          h[n] = 1
      res = max(h.values())
      
        
          
      return -1 if res < 2 else res        