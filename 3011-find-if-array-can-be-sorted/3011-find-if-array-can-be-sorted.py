class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
      
      # function count bits in number
      def count_bits(n):
        return bin(n).count("1")
      
      n = len(nums)
      
      for i in range(n):
        flag = False
        
        for j in range(n - i - 1):
          # if already sorted
          if nums[j] <= nums[j+1]:
            continue
          
          # Swap the elements
          if count_bits(nums[j]) == count_bits(nums[j+1]):
            nums[j], nums[j+1] = nums[j+1], nums[j]
            flag = True
          else:
            return False
        # this flag means that array is already sorted
        if not flag:
          break
      return True
        