class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = {}
        res = 0
        
        for i in J:
            d[i] = 0
            
        for i in S:
            if i in d:
                res += 1
                
        return res
