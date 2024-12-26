class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
      sums =[0, 0]
      
      for n in nums:
        if n < 10:
          sums[0] += n
        else:
          sums[1] += n
      
      return sums[0] != sums[1]
        