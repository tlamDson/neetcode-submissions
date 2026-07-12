# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        resSubRoot = []
        resRoot = []
        self.dfs(subRoot, resSubRoot)
        self.dfs(root, resRoot)
        full_tree_str = ",".join(resRoot)
        sub_tree_str = ",".join(resSubRoot)
        return f",{sub_tree_str}," in f",{full_tree_str},"

       

    def dfs(self, node : Optional[TreeNode],result : list):
        if not node:
            result.append("null")
            return
        result.append(str(node.val))
        self.dfs(node.left, result )

        self.dfs(node.right,result )

        