class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''.join([str(n) for n in digits])
        number = list(str(int(number) + 1))
        return number
