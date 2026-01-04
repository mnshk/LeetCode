/**
 * Approach: Two Pass Approach or Iterative counting approach
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class Solution1 {
    ListNode middleNode(ListNode head) {
        int length = 0;
        ListNode curr = head;
        while (curr != null) {
            length += 1;
            curr = curr.next;
        }
        length = Math.floorDiv(length, 2);
        curr = head;
        while (length != 0) {
            curr = curr.next;
            length -= 1;
        }
        return curr;
    }
}
