from typing import List


class Solution2:

    # O(n) time complexity
    # O(1) space complexity
    def majorityElement(self, nums: List[int]) -> int:

        candidate = nums[0]
        dominance = 0

        # Boyer-Moore's Majority Vote Algorithm
        for num in nums:
            # If there is no dominance
            if dominance == 0:
                # then current number can be the candidate
                candidate = num

            # If the current number is the candidate
            if candidate == num:
                # It's dominance will increase
                dominance += 1
            # Otherwise
            else:
                # It's dominance will decrease
                dominance -= 1

        return candidate
