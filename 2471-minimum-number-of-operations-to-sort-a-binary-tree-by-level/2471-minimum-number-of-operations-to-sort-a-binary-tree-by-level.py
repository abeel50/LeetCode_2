# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:     
      
      def countSwaps(arr):
        swaps = 0
        sorted_arr = sorted(arr)
        idx_map = {n:i for i, n in enumerate(arr)}
        
        for i in range(len(arr)):
          if arr[i] != sorted_arr[i]:
            swaps += 1
            
            j = idx_map[sorted_arr[i]]
            arr[i], arr[j] = arr[j], arr[i]
            idx_map[arr[j]] = j
        return swaps
        
      q = deque([root])
      res = 0
      while q:
        level = []
          
        for _ in range(len(q)):
          node = q.popleft()
          level.append(node.val)
          if node.left:
            q.append(node.left)
          if node.right:
            q.append(node.right)
        res += countSwaps(level)
              
      return res
        