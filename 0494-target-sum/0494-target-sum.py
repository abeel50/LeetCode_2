class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
      cache = {}
      
      def findTargetSum(i, s):
        if (i,s) in cache:
          return cache[(i,s)]
        
        if i == len(nums):
          return 1 if s == target else 0
      
        
        cache[(i,s)] = (findTargetSum(i+1, s + nums[i]) + 
        findTargetSum(i + 1, s - nums[i]))
        return cache[(i, s)]
      
      
      return findTargetSum(0, 0) 