from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Time complexity: O(N)
        Space complexity: O(N)
        """

        # Create a hash set for quick lookup
        curr_nums = set(nums)

        # Check if every number is in the list or not sequently
        for i in range(1, len(nums)+1):
            # If not return that number
            if i not in curr_nums:
                return i
        return 0
