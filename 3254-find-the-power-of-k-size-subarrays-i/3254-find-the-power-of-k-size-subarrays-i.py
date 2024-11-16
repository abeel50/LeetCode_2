class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
      
      def isConsecutive(sub):
          if not sub:
              return -1

          for i in range(1, len(sub)):
              if sub[i] != sub[i - 1] + 1:
                  return -1

          return sub[-1]
      
      res = []
      for i in range(len(nums) - k + 1):
        res.append(isConsecutive(nums[i: i + k]))
      return res