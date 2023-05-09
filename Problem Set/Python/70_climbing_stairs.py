class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 0, 1
        count = 1
        while count <= n:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return nth
