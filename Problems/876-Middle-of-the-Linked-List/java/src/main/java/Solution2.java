/**
 * Approach: Two pointers (Fast & Slow) based on Floyd's Cycle Detection Algorithm (Tortoise and the Hare)
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 * */
public class Solution2<T> {
    public ListNode<T> middleNode(ListNode<T> head) {
        ListNode<T> slow = head;
        ListNode<T> fast = head;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}
