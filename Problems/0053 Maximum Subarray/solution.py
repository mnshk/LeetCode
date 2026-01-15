from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time complexity: O(N)
        Space complexity: O(1)
        """

        # If there were only positive numbers in this list
        # then the maximum sub-array sum would always have been the sum of the entire list.

        # O(1) space complexity and O(n) time complexity solution
        # Kadane's Algorithm.

        # Initialize the initial maximum sum to be the first number
        # It cannot be initialized to 0 because the maximum sum can even be less than zero.
        max_sum = nums[0]

        curr_sum = 0

        for num in nums:
            # If the current sum is negative, we can do a fresh start,
            # there is no point of dragging a negative sum along.
            if curr_sum < 0:
                curr_sum = 0
            # Add current number to the sum
            curr_sum += num
            # Update the maximum sum seen so far
            max_sum = max(max_sum, curr_sum)

        return max_sum
