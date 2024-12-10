class Solution:
    def maximumLength(self, s: str) -> int:
      # Dictionary to store the count of special substrings
      special_counts = defaultdict(int)
      res = -1
      # Iterate over all possible substrings
      for i in range(len(s)):
          for j in range(i + 1, len(s) + 1):
              substring = s[i:j]

              # Check if the substring is special
              if len(set(substring)) == 1:
                  special_counts[substring] += 1
                  if special_counts[substring] >=3:
                    res = max(res, len(substring))
      return res
        