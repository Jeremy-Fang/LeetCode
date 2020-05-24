class Solution:
    def reverseVowels(self, s: str) -> str:
        char_arr = list(s)
        l = 0
        r = len(char_arr)-1
        v = {'a','e','i','o','u', \
             'A','E','I','O','U'}
        
        while l < r:
            while l < r and char_arr[l] not in v:
                l += 1
            while l < r and char_arr[r] not in v:
                r -= 1
            if l < r:
                t = char_arr[l]
                char_arr[l] = char_arr[r]
                char_arr[r] = t
                l += 1
                r -= 1
        
        return ''.join(char_arr)
