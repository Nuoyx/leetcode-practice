/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null){
            return head;
        }
        if(head.next == null){
            return head;
        }
        ListNode newHead = reverseListHelper(head);
        head.next = null;
        return newHead;
    }

    ListNode reverseListHelper(ListNode temp){
        if(temp.next == null){
            return temp;
        }
        ListNode tempNext = temp.next;
        ListNode newHead = reverseListHelper(tempNext);
        tempNext.next = temp;
        return newHead;

    }
}