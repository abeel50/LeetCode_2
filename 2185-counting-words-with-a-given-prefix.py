class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
      def isPrefix(w1, w2):
        for i, c in enumerate(w1):
          if i >= len(w2) or w2[i] != c:
            return False
  
        return True
    
      res = 0
      for w in words:
        if isPrefix(pref, w):
          res += 1
      return res
        
