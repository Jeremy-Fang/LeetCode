class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        N = len(s)//2
        v = {'a','e','i','o','u'}
        s1 = s[0:N]
        s2 = s[N:]
        res1 = res2 = 0
        
        for c in s[0:N]:
            res1 += (c.lower() in v)
            
        for c in s[N:]:
            res2 += (c.lower() in v)
        
        return res1 == res2
        
