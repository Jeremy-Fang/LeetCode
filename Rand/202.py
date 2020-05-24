class Solution:
    def isHappy(self, n: int) -> bool:
        i = [int(i) for i in str(n)]
        n = n
        d = set()
        
        while n != 1:
            n = sum([int(i)*int(i) for i in str(n)])
            if n in d:
                return False
            d.add(n)
            
        return True
