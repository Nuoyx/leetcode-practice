# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def sumNumbersHelper(prev, root):
            if root is None:
                return prev
            prev = prev * 10 + root.val
            if root.left is None:
                return sumNumbersHelper(prev, root.right)
            elif root.right is None:
                return sumNumbersHelper(prev, root.left)
            else:
                return sumNumbersHelper(prev, root.left) + sumNumbersHelper(prev, root.right)

        return sumNumbersHelper(0, root)
