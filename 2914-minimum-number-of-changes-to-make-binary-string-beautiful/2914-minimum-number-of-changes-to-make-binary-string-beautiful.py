class Solution:
    def minChanges(self, s: str) -> int:
      LEN = len(s)
      res = 0
      if LEN % 2 != 0:
        return res
      
      for i in range(0, LEN, 2):
        if s[i] != s[i+1]:
          res += 1
      return res
        
      
        