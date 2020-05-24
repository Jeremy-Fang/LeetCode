class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        N = len(s)
        d = collections.defaultdict(chr)
        
        for i in range(1,27):
            if i < 10:
                d[str(i)] = chr(97+i-1)
            else:
                d[(str(i)+"#")] = chr(97+i-1) 
        
        for i in range(N):
            if s[i] == "#":
                res.pop()
                res.pop()
                res.append(s[i-2:i+1])
            else:
                res.append(s[i])
        
        return "".join([d[i] for i in res])
