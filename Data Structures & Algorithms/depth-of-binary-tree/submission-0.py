# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #To calculate the heihg of a hnode, i need the results from its children first. Post-order traversa lefgtt, right root allows me to visti childeren before processing the parent


        if not root:
            return 0
        
        # Calculate height of left and right subtrees
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        return 1 + max(left_height, right_height)
        