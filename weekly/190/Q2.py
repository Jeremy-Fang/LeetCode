class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = 0
        ma = 0
        N = len(s)
        curr = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        for end in range(N):
            if s[end] in vowels:
                curr += 1
                
            if end >= k:
                if s[start] in vowels:
                    curr -= 1
                start += 1
            ma = max(ma, curr)
                
        return ma
