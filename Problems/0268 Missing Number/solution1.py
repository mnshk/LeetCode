from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Time complexity: O(N) or O(2N)
        Space complexity: O(1)
        """

        actual_sum = 0
        # Compute the actual some of the list without a number being missing
        for i in range(1, len(nums)):
            actual_sum += i

        curr_sum = 0
        # Compute the current sum of the list
        for num in nums:
            curr_sum += num

        # The missing number is the difference between the actual sum and the present sum
        return actual_sum - curr_sum
