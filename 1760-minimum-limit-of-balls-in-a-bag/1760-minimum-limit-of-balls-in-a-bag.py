class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
      
      def isGood(balls):
        ops = 0
        for n in nums:
          ops += ceil(n/balls) - 1
          if ops > maxOperations:
            return False
        return True
      
      l, r = 1, max(nums)
      
      while l < r:
        mid = (l+r) // 2
        
        if isGood(mid):
          r = mid
          
        else:
          l = mid + 1
      return l
                