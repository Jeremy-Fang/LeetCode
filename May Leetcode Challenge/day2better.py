class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0
        
        for j in J:
            res += len(S.split(j)) - 1
            print(S.split(j))
            
        return res
