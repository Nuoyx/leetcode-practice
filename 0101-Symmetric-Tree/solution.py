# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if(root == None):
            return True
        temp = self.checkSymmetric(root.left, root.right)
        return temp
        
    
    
    def checkSymmetric(self, left, right):
        """
        :type left: Optional[TreeNode]
        :type right: Optional[TreeNode]
        :rtype: bool
        """
        temp = True
        if(left == None and right == None):
            return True
        elif(left == None or right == None):
            return False
        if left.val == right.val:
            temp = self.checkSymmetric(left.left, right.right)
        else:
            return False
        if temp:
            temp = self.checkSymmetric(left.right, right.left)
        return temp