class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_p = ""
        for i in range(len(min(strs))):
            firstLetter = [x[0:i+1] for x in strs]
            if len(set(firstLetter)) == 1:
                max_p = firstLetter[0]
        return max_p
