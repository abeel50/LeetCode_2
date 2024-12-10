class Solution:
    def maximumLength(self, s: str) -> int:
      # Dictionary to store the count of special substrings
      special_counts = defaultdict(int)

      # Iterate over all possible substrings
      for i in range(len(s)):
          for j in range(i + 1, len(s) + 1):
              substring = s[i:j]

              # Check if the substring is special
              if len(set(substring)) == 1:
                  special_counts[substring] += 1

      # Filter substrings that occur at least thrice
      valid_specials = [key for key, count in special_counts.items() if count >= 3]

      # Find the length of the longest special substring
      if not valid_specials:
          return -1
      else:
          return max(len(sub) for sub in valid_specials)
        