class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        
        if not intervals:
            return []
        
        intervals.sort(key=lambda e: (e[0], e[1]))
        
        mi = ma = None
        
        for start, end in intervals:
            if mi == None:
                mi = start
                ma = end
                
            if start <= ma:
                ma = max(ma, end)
            else:
                res.append([mi, ma])
                mi = start
                ma = end
        
        res.append([mi, ma])
        
        return res
