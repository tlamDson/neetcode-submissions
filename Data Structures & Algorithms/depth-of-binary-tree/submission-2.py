# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        stack = deque([(root, 1)])       
        res = 1
        while stack:
            node, depth = stack.popleft()
            if node:
                res = max(res, depth)
                stack.append([node.right,depth + 1])
                stack.append([node.left, depth + 1])
        return res
    