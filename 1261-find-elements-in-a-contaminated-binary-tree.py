# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.hash = set() 
        self.hash.add(root.val)
        self.tree = self.recover(root)    

    def find(self, target: int) -> bool:
        return target in self.hash

    def recover(self, node: Optional[TreeNode]):
        if node:
            if node.left:
                node.left.val = 2 * node.val + 1
                self.hash.add(node.left.val)
                node.left = self.recover(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                self.hash.add(node.right.val)
                node.right = self.recover(node.right)
        return node


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
