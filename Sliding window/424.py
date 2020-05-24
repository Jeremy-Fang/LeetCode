class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        L = len(s)
        d = collections.defaultdict(int)
        curr_most = ""
        ma = 0
        
        while r < L:
            d[s[r]] += 1
            
            if curr_most not in d or d[s[r]] >= d[curr_most]:
                curr_most = s[r]
            
            while l < r and r - l - d[curr_most] + 1 > k:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1
                    
            ma = max(ma, r - l + 1)
            r += 1
            
        return ma
