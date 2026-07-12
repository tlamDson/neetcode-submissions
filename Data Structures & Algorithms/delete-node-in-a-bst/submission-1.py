# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getMin(node):
            curr = node
            while curr and curr.left:
                curr = curr.left
            return curr
        if not root: return None
        if root.val ==  key:
            if not root.left: return root.right
            if not root.right: return root.left
            successor = getMin(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right,successor.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)
        return root

        