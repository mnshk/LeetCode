# 543 - Diameter of Binary Tree

### Definitions

- The diameter of a binary tree is the length of the longest path between any two nodes in the tree.

- The path may or may not pass through the root.

- A node cannot be visited more than once. Otherwise, the path length would be unbounded due to cycles (which trees do not have).

- The length of a path is measured in number of edges, not nodes.

### How can we calculate the diameter?

For any node we can calculate what is the longest path that this node is a part of.

Which means if a path was passing through this node from left to right, it's length can be calculated by adding the height of it's left subtree to the height or it's right subtree

i.e. Not any path but the longest path passing through this node is:

`curr_longest_path = height(self.left) + height(self.right)`

So, for each node we can calculate the longest path passing through this node and keep track of the longest we've seen.

And the tree's diameter is simply the maximum of this value across all nodes.

`longest_path = max(longest_path, curr_longest_path)`

### Solution 1:

We can traverse all of the nodes in the tree and for each call the height function with it's left and right subtree to get the `curr_longest_path`

But these are a lot of calls to `height()`. To calculate the height of root, we are already traversing all of the children nodes or entire tree.

In worst case this leads to a `O(N^2)` time complexity.

## Solution 2: Optimal

But for each node the `height()` function will traverse all of it's children nodes asking for their heights. And the height function do have access to the heights of the left and right subtrees of the current node. Which means we can make the height function keep track of the longest path it has seen so far.

But we do not have to calculate call the `height()` function on each and every node. Because recursively it will call itself on the children nodes of the given node to calculate the height.

Each node is visited exactly once. Which turns the time complexity all the way down to `O(N)`
