class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
      
      def transform(n):
        steps = 0
        while n != 1:
          if n % 2 == 0:
            n = n / 2
          else:
            n = 3*n + 1
          steps += 1
        return steps
      
      arr = {}
      for n in range(lo, hi + 1):
        arr[n] = transform(n)
      arr = dict(sorted(arr.items(), key=lambda item: item[1]))

      return list(arr.keys())[k-1]