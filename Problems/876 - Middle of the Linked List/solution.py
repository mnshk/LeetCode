from typing import Optional
from util import *


class Solution:
    def middleNode(self, head: Optional[ListNode[int]]) -> Optional[ListNode[int]]:

        # Initialize both slow and fast pointers pointing to head
        slow = head
        fast = head

        # While fast pointer is not None and the next of the fast pointer is not None
        while fast and fast.next:
            # For the sake of strict typing
            assert slow is not None

            # Move slow pointer one step
            slow = slow.next
            # Move fast pointer two steps
            fast = fast.next.next

        # Once fast pointer reaches the end of the LinkedList
        # The slow pointer will be at the center
        return slow
