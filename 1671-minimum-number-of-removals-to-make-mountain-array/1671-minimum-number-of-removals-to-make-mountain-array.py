class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
      N = len(nums)
      
      # longest increasing sub sequence
      lis = [1] * N
      for i in range (N):
        for j in range(i):
          if nums[j] < nums[i]:
            lis[i] = max(lis[i], 1 + lis[j])
            
      #longest decresing subsequence
      lds = [1] * N
      for i in reversed(range(N)):
        for j in range (i+1, N):
          if nums[j] < nums[i]:
            lds[i] = max(lds[i], 1 + lds[j])
            
      res = N
      for i in range(1, N-1):
        if min (lds[i], lis[i]) > 1:
          res = min (res , N - lds[i] - lis[i] + 1)
      
      return res  