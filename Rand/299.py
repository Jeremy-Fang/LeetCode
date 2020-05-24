class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        
        g = collections.Counter()
        s = collections.Counter()
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            g[guess[i]] += 1
            s[secret[i]] += 1
        
        for i in s.keys():
            cows += min(s[i], g[i])
            
        return str(bulls) + "A" + str(cows-bulls) + "B"
