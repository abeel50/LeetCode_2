class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
      res = 0
      curMax = -1
      
      for i,n in enumerate(arr):
        curMax = max(curMax, n)
        if curMax == i:
          res += 1
          
      return res 