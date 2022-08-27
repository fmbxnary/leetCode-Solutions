class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        sum = 0
        for i in range(len(s) - 1):
            left = s[i]
            right = s[i + 1]
            if values[left] < values[right]:
                sum -= values[left]
            else:
                sum += values[left]
        sum += values[s[-1]]
        return sum
