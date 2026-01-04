from typing import Optional
from helpers import ListNode


class Solution1:
    """
    Approach: Two Pass Approach or Iterative counting approach
    Time complexity: O(N)
    Space complexity: O(1)

    Logic: Calculate the length of the list, 
    then traverse till the half of the length to find the middle node.
    """

    def middleNode(self, head: Optional[ListNode[int]]) -> Optional[ListNode[int]]:

        length = 0
        curr = head
        # Measure the length of the list
        while curr:
            length += 1
            curr = curr.next
        # Calculate the half length
        length = length // 2
        # Reset current to the start of the list
        curr = head
        # Move forward till we reach the middle
        while curr and length:
            curr = curr.next
            length -= 1
        # Return the middle node
        return curr
