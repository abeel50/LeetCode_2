class Solution:
  def compressedString(self, word: str) -> str:
      if not word:
          return ""

      comp = []
      count = 1
      prv = word[0]

      for c in word[1:]:
          if c == prv:
              count += 1
              if count == 9:
                  comp.append(f"{count}{prv}")
                  count = 0
          else:
              if count > 0:
                  comp.append(f"{count}{prv}")
              prv = c
              count = 1

      if count > 0:
          comp.append(f"{count}{prv}")

      return ''.join(comp)

        