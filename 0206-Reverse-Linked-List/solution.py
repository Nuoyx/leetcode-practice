# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head
        temp_list = []
        end = -1
        while(temp != None):
            temp_list.append(temp.val)
            temp = temp.next
        temp = head
        for i in range(len(temp_list)):
            temp.val = temp_list[end - i]
            temp = temp.next
        return head