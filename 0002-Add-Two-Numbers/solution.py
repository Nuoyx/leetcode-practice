# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = l1
        overflow = False
        if result == None:
            result = ListNode()
        if l2.val != None:
            result.val += l2.val
            l2 = l2.next
        if(result.val > 9):
            result.val -= 10
            overflow = True
        temp = result
        while l2 is not None or overflow:
            if temp.next == None:
                temp.next = ListNode()
            temp = temp.next
            if overflow:
                temp.val += 1
                overflow = False
            
            if l2 is not None:
                temp.val += l2.val
                l2 = l2.next
            
            if(temp.val > 9):
                temp.val -= 10
                overflow = True
                
            
        
        return result