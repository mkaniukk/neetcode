# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root.left and root.right:
            return (
                2
                + self.diameterOfBinaryTree(root.left)
                + self.diameterOfBinaryTree(root.right)
            )

        if root.left and not root.right:
            return 1 + self.diameterOfBinaryTree(root.left)

        if not root.left and root.right:
            return 1 + self.diameterOfBinaryTree(root.right)
