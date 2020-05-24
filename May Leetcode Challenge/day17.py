class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pd = collections.defaultdict(int)
        l = r = 0
        N = len(s)
        L = len(p)
        curr = collections.defaultdict(int)
        res = []
        
        for i in p:
            pd[i] += 1
        
        
        while r < N:
            curr[s[r]] += 1
            while curr[s[r]] > pd[s[r]]:
                curr[s[l]] -= 1
                l += 1
            if r - l + 1 == L:
                res.append(l)
                        
            r += 1
            
        return res
            
