from typing import Optional, List, Generic, TypeVar

T = TypeVar("T")


class ListNode(Generic[T]):
    def __init__(self, val: Optional[T] = None, next: Optional[ListNode[T]] = None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(items: List[T]) -> Optional[ListNode[T]]:
        head = ListNode[T]()
        curr = head
        for item in items:
            curr.next = ListNode(item)
            curr = curr.next
        return head.next

    @staticmethod
    def to_list(head: Optional[ListNode[T]]) -> List[Optional[T]]:
        result: List[Optional[T]] = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
