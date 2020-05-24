class Solution:
    def arrangeWords(self, text: str) -> str:
        words = sorted([i.lower() for i in text.split(' ')], key=lambda i: len(i))
        words[0] = words[0].capitalize()
        res = ""
        
        for i in range(len(words) - 1):
            res += words[i] + ' '
            
        return res + words[-1]
