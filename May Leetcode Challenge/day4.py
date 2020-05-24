class Solution:
    def findComplement(self, num: int) -> int:
        x = math.floor(math.log(num, 2)) + 1
        
        return max(0, 2**x - num - 1)
