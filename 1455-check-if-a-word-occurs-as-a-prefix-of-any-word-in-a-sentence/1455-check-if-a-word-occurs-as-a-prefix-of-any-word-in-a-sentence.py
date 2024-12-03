class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
      words = sentence.split(' ')
      
      for i,w in enumerate(words):
        match = False
        for j, s in enumerate(searchWord):
          if j >= len(w) or w[j] != s:
            match = False
            break
          else:
            match = True
        if match:
          return i + 1
             
      return -1
        
        