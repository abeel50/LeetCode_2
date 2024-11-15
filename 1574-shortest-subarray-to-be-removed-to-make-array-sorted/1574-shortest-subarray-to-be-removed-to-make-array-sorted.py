class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
      n = len(arr)
      left, right = 0, n - 1

      # Find the left-most part that is non-decreasing
      while left < n - 1 and arr[left] <= arr[left + 1]:
          left += 1

      if left == n - 1:
          return 0  # The array is already non-decreasing

      # Find the right-most part that is non-decreasing
      while right > 0 and arr[right] >= arr[right - 1]:
          right -= 1

      # Minimum length to remove is either removing left or right part
      result = min(n - left - 1, right)

      # Try to merge left part and right part
      i, j = 0, right
      while i <= left and j < n:
          if arr[i] <= arr[j]:
              result = min(result, j - i - 1)
              i += 1
          else:
              j += 1

      return result
        