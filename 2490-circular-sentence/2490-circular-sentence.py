class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
      words = sentence.split()

      # Check the first and last characters of the first and last words
      if words[0][0] != words[-1][-1]:
          return False

      # Check that each word ends with the starting character of the next word
      for i in range(len(words) - 1):
          if words[i][-1] != words[i + 1][0]:
              return False

      return True
