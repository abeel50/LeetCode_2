class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
      def isPrime(n):
        for f in range(2, int(sqrt(n)) + 1):
          if n % f == 0:
            return False
        return True
      
      prv = 0
      for n in nums:
        upper_bound = n - prv
        
        largest_prime = 0
        for i in reversed(range(2, upper_bound)):
          if isPrime(i):
            largest_prime = i
            break
        
        if n - largest_prime <= prv:
          return False
        
        prv = n - largest_prime
      
      return True
          
        