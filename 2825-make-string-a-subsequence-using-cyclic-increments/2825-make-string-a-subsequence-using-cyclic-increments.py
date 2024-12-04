class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
      alphabates = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
      i, j = 0, 0
      
      while i < len(str1) and j < len(str2):
        c1, c2 = str1[i] , str2[j]
        if c1 == c2:
          i += 1
          j += 1
          continue
        c1 = alphabates[(alphabates.index(c1) + 1) % 26]
        if c1 == c2:
          i += 1
          j += 1
          continue
          
        i += 1
      
      return j >= len(str2)        