from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution2:
    """
    Approach: 

    Diameter is the longest path which can be formed in a tree.

    For every node we can check if that node is a part of the diameter
    by adding the height of it's left and right subtrees.
    So for each node if the path it forms from left to right
    can be compared against the maximum path seen.


    Time Complexity: O(N) -> Each node is visited exactly once.
    Space Complexity: O(1)
    """

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Keep track of the maximum diameter seen
        max_dia = 0

        def height(root: Optional[TreeNode]) -> int:
            """
            Function that calculates height of a node, but also
            keeps track of the length of the diameter passing through the current node.
            """
            # If no element, height is zero
            if not root:
                return 0

            # Calculate heights
            left_height = height(root.left)
            right_height = height(root.right)
            self_height = max(left_height, right_height)+1

            # If this was the node the diameter was passing through
            dia_passing_this_node = left_height + right_height

            # Update max_dia if it's greater than the current max
            nonlocal max_dia
            max_dia = max(max_dia, dia_passing_this_node)

            # Return the height of the current node
            return self_height

        height(root)

        return max_dia
