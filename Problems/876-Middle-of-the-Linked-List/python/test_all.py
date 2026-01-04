from typing import Type
from helpers import ListNode
from solution_1 import Solution1
from solution_2 import Solution2
import pytest


@pytest.mark.parametrize("solution_class", [Solution1, Solution2])
def test_middle_node(solution_class: Type[Solution1]):

    ln = ListNode[int]
    solution = solution_class()

    head = ln.from_list([1])
    result = solution.middleNode(head)
    assert ln.to_list(result) == [1]

    head = ln.from_list([1, 2, 3, 4, 5])
    result = solution.middleNode(head)
    assert ln.to_list(result) == [3, 4, 5]

    head = ln.from_list([1, 2, 3, 4, 5, 6])
    result = solution.middleNode(head)
    assert ln.to_list(result) == [4, 5, 6]

    head = ln.from_list([1, 2])
    result = solution.middleNode(head)
    assert ln.to_list(result) == [2]
