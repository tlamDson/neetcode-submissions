# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        result =  self.getHeight(root)
        return result != -1

    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left,right)
        
    
