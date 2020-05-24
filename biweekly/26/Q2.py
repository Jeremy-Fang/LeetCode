class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        
        if n == 1:
            return []
        
        for den in range(2, n + 1):
            for num in range(1, den):
                if math.gcd(num, den) == 1:
                    res.append(str(num) + "/" + str(den))
                    
                    
        return res
