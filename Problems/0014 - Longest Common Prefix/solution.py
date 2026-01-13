from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Assume the first string is the longest common prefix
        # Then for each string I will compare that to the common prefix from left to right
        # and slice the longest common prefix where it stops being equal to the character at that index in string
        # If at any point I encounter a string to be empty of my longest common prefix got empty, I will return empty string

        # As per constraints there is at least one string
        lcp = strs[0]

        # Start from the second string
        # O(NxM)
        for i in range(1, len(strs)):
            curr = strs[i]

            # Early exit if any of them is empty return
            if lcp == "" or curr == "":
                return ""

            new_lcp = []

            # Loop j till the end of the shortest string
            # O(M)
            for j in range(min(len(lcp), len(curr))):
                # If characters match keep going
                if lcp[j] == curr[j]:
                    new_lcp.append(lcp[j])
                else:
                    # Otherwise stop
                    break

            # Update the LCP
            lcp = "".join(new_lcp)

        return lcp
