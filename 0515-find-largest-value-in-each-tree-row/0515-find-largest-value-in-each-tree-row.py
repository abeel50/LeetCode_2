# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
      if not root:
        return []
      q = deque([root])
      
      res = []
      while q and len(q) > 0:
        rowMax = q[0].val
        for i in range(1, len(q)):
          rowMax = max(rowMax, q[i].val)
        res.append(rowMax)
        
        for _ in range(len(q)):
          node = q.popleft()
          if node.left:
            q.append(node.left)
          if node.right:
            q.append(node.right)
              
      
      return res 