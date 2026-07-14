# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # chạy từ root của 2 cây và verify
        queue = deque([(p,q)])
        while queue:
            p, q = queue.popleft()
            # pop ma la none thi se gay loi
            if not p and not q:
                continue
            if (not p and q) or (p and not q):
                return False
            if p.val != q.val:
                return False
            # hãy xử lí none ở đầu thay vì chek none để append
            queue.append((p.left, q.left))
            queue.append((p.right, q.right))
        return True

            
        