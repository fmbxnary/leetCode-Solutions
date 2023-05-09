class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pr = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for c in s:
            if c in pr.keys():
                stack.append(c)
            else:
                if not stack:
                    return False
                l = stack[-1]
                if not c == pr[l]:
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        return False
