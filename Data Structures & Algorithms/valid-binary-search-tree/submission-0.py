# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def dfs(node,low,high):
            if not node: return True
            if node.val <= low or node.val >= high:
                return False
            return  dfs(node.right,node.val,high) and dfs(node.left,low,node.val)
        return dfs(root,float("-inf"),float("inf"))
        


        
            
        