/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;

        if (l1 == null && l2 == null) {
            return null;
        }

        ListNode sum = new ListNode();
        if (l1 == null) {
            l1 = new ListNode(0);
        }
        else if (l2 == null) {
            l2 = new ListNode(0);
        }
        sum.val = (l1.val + l2.val) % 10;
        carry = (l1.val + l2.val >= 10) ? 1 : 0;

        if (carry == 1) {
            if (l1.next != null) { 
                l1.next.val += 1;
            }
            else {
                l1.next = new ListNode(1);
            }
            sum.next = AddTwoNumbers(l1.next, l2.next);
        }
        else {
            sum.next = AddTwoNumbers(l1.next, l2.next);
        }
        return sum;
    }
}