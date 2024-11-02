class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
      words = sentence.split(' ')
      if len(words) == 1:
        return words[0][0] == words[0][-1]
      i, j = 0, 1
      
      while i < len(words) and j <= len(words)-1:
        last, first = words[i][-1], words[j][0]
        if last != first:
          return False
        i += 1
        j += 1
      return words[0][0] == words [-1][-1]
        