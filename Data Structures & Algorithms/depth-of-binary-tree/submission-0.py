# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:
        if root == None:
            return depth

        maximum = depth

        maxLeft = self.maxDepth(root.left, depth=depth + 1)
        maxRight = self.maxDepth(root.right, depth=depth + 1)

        maximum = max(maxLeft, maxRight)

        return maximum