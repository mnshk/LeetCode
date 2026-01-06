from collections import deque
from typing import Optional, Dict
from solution_2 import TreeNode


class Solution1:
    """
    Approach:

    For each node we calculate what would be the longest
    path passing through this node.

    Note: There is another optimal way to keep track of the longest path
    seen within the height function, implemented in second solution.

    Time complexity: O(N) ( O(N^2) without memoization )
    Space complexity: O(N) -> For memo

    """

    memo: Dict[TreeNode, int] = dict()

    def height(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        if root in self.memo:
            return self.memo[root]

        self.memo[root] = max(
            self.height(root.left),
            self.height(root.right)
        )+1
        return self.memo[root]

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        queue = deque([root])
        max_dia = 0

        while queue:
            curr = queue.popleft()

            dia_passing_curr = self.height(curr.left) + self.height(curr.right)
            max_dia = max(max_dia, dia_passing_curr)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return max_dia
