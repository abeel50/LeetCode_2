# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        st = [] #stack
        dashCount, i =  0, 0

        while i < len(traversal):
            # if charcter is "-" we count the dashes
            if traversal[i] == '-':
                dashCount += 1
                i += 1
            else:
                j = i
                # we extract the integer and make a Tree node
                while j < len(traversal) and traversal[j] != '-':
                    j += 1
                node = TreeNode(int(traversal[i:j]))

                # Sepending upon number of depth we pop curret stack items
                while len(st) > dashCount:
                    st.pop()
                #reached at required depth first check left 
                if st and not st[-1].left:
                    st[-1].left = node
                elif st:
                    #else add to right
                    st[-1].right = node
                #append the node as well
                st.append(node)
                
                #move i to end of integer reste the dash
                i = j
                dashCount = 0
        return st[0]     
