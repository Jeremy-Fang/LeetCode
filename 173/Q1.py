class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def pali(s):
            return s == s[::-1]
        
        if s == "":
            return 0
        
        if pali(s):
            return 1
        return 2
