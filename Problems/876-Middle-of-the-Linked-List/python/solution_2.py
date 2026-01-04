from typing import Optional
from helpers import ListNode


class Solution2:
    """
    Approach: Two pointers (Fast & Slow) based on Floyd's Cycle Detection Algorithm (Tortoise and the Hare)
    Time complexity: O(N)
    Space complexity: O(1)

    Logic: By the time the fast pointer reaches the end,
    the slow pointer will be exactly at the midpoint.
    """

    def middleNode(self, head: Optional[ListNode[int]]) -> Optional[ListNode[int]]:

        # Initialize both slow and fast pointers pointing to head
        slow = head
        fast = head

        # While fast pointer is not None and the next of the fast pointer is not None
        while slow and fast and fast.next:
            # Move slow pointer one step
            slow = slow.next
            # Move fast pointer two steps
            fast = fast.next.next

        # Return the slow pointer which will be at the center
        return slow
