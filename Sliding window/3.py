class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        L = len(s)
        d = set()
        ma = 0
        
        while r < L:
            if s[r] in d:
                while l < r and s[l] != s[r]:
                    d.remove(s[l])
                    l += 1
                l += 1
            d.add(s[r])
            r += 1
            ma = max(ma, r - l)
            
        return ma
