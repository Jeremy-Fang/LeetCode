class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = collections.Counter(arr)
        res = len(c)
        
        for i in sorted(c.keys(), key=lambda i: c[i]):
            if k >= c[i]:
                res -= 1
                k -= c[i]
            else:
                break
            
        return res
