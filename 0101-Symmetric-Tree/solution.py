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
      
      
      
      
# Optimized version:
# class Solution:
#   def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      
#       def is_mirror(n1, n2): # n1:left, n2:right
#           if not n1 and not n2:
#               return True
          
#           if not n1 or not n2:
#               return False
          
#           return n1.val == n2.val and is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)
      
#       return is_mirror(root.left, root.right)