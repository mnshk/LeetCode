from util import *
from solution import *


def test_single_node():
    head = ListNode[int].from_list([1])
    assert ListNode[int].to_list(Solution().middleNode(head)) == [1]


def test_odd_length():
    head = ListNode[int].from_list([1, 2, 3, 4, 5])
    assert ListNode[int].to_list(Solution().middleNode(head)) == [3, 4, 5]


def test_even_length():
    head = ListNode[int].from_list([1, 2, 3, 4, 5, 6])
    assert ListNode[int].to_list(Solution().middleNode(head)) == [4, 5, 6]


def test_two_nodes():
    head = ListNode[int].from_list([1, 2])
    assert ListNode[int].to_list(Solution().middleNode(head)) == [2]


def main():
    test_single_node()
    test_even_length()
    test_odd_length()
    test_two_nodes()


if __name__ == "__main__":
    main()
