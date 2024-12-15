class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
      def findMaxDigit(n):
        largest_digit = 0
        totalDigits = 0
        while (n):        
          digit = n % 10
          largest_digit = max(digit, largest_digit)
          n = n // 10
          totalDigits += 1

        return int(str(largest_digit) * totalDigits)
      
      return sum([findMaxDigit(n) for n in nums ])      