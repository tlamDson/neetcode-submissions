# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalance = True
        if not root:
            return self.isBalance
        def getHeight(root):
            if not root:
                return self.isBalance
            left = getHeight(root.left)
            right = getHeight(root.right)
            if abs(left - right) > 1:
                self.isBalance = False
            return 1 + max(left,right)
        getHeight(root)
        return self.isBalance
        