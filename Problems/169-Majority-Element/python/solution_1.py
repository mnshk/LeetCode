from typing import List, Dict
from collections import defaultdict


class Solution1:

    # O(n) time complexity
    # O(n) space complexity
    def majorityElement(self, nums: List[int]) -> int:

        freq: Dict[int, int] = defaultdict()

        for num in nums:
            # Update frequency of the element
            freq[num] += 1
            # If element's frequency is more than the n/2, return
            if freq[num] > len(nums)//2:
                return num
        return -1
