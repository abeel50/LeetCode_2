class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
      
      def isConsecutive(sub):
        m = sub[0]
        prv = sub[0]
        for i in range(1, len(sub)):
          if sub[i] == prv + 1:
            m = max(m, sub[i])
            prv = sub[i]
          else:
            return -1
        return m
      
      res = []
      for i in range(len(nums) - k + 1):
        # print(nums[i:i+k], isConsecutive(nums[i: i + k]))
        res.append(isConsecutive(nums[i: i + k]))
      return res