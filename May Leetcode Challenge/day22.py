class Solution:
    def frequencySort(self, s: str) -> str:
        d = collections.defaultdict(int)
        res = ""
        
        for c in s:
            d[c] -= 1
        
        if len(d) == 0:
            return ""
        
        for c in sorted(d.keys(), key=lambda i: d[i]):
            res += (c * (-d[c]))
            
        return res
