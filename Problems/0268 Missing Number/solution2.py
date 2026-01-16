from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Time complexity: O(N)
        Space complexity: O(1)
        """

        n = len(nums)
        # Compute the actual sum using the formula of the sum of N natural numbers
        actual_sum = int((n * (n + 1)) / 2)

        curr_sum = 0
        # Compute the current sum of the list
        for num in nums:
            curr_sum += num

        # The missing number is the difference between the actual sum and the present sum
        return actual_sum - curr_sum
