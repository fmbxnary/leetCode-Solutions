class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = ""
        max_ss = ""

        for c in s:
            if c not in ss:
                ss += c
            else:
                ss = ss[ss.index(c) + 1:] + c
            if len(ss) >= len(max_ss):
                max_ss = ss
        return len(max_ss)
