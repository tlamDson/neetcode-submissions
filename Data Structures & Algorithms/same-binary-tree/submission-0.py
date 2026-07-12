# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        valP, valQ = [],[]
        self.dfs(p, valP)
        self.dfs(q, valQ)
        if valP != valQ:
            return False
        else:
            return True
        
        
      
        
    def dfs(self, node: Optional[TreeNode], result : list):
        if not node:
            result.append("null")
            return 
        result.append(str(node.val))
        self.dfs(node.left, result)
        self.dfs(node.right, result)
    
        