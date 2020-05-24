class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        start  = end = None
        res = 0
        
        if duration == 0 or not timeSeries:
            return 0
        
        for time in timeSeries:
            if start == None:
                start = time
                end = time + duration
            else:
                if time >= end:
                    res += end - start
                    start = time
                    end = time + duration
                else:
                    end = time + duration
        
        res += end - start
        
        return res
