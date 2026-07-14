# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(p,q):
            queue = deque([(p,q)])
            while queue:
                p,q = queue.popleft()
                if not p and not q: 
                    continue
                if (not p and q) or (p and not q):
                    return False
                if p.val != q.val:
                    return False
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
            return True
        if not subRoot: return True
        if not root: return False
        if check(root,subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

            
        