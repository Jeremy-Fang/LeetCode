class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        
        if n == 1:
            return start
        
        for i in range(n): 
            res ^= start + 2*i
            
        return res
