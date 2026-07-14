# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # tại mỗi node thì duyệt xem balacne không
        # dfs trả về gì trả về độ dài 
        
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            if left == -1: return -1
            right = dfs(node.right)
            if right == -1: return -1
            if abs(left - right) > 1:
                # cái abs(left - right) vẫn chạy được tuy nhiên lần sau sẽ là max (false, right)
                # nếu sai từ đó sẽ sai
                return -1
            return 1 + max(left, right)
        return dfs(root) != -1
        
        