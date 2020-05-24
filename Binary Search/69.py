class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        l = 1
        r = x
        
        while l < r:
            mid = (l + r) // 2
            if mid ** 2 > x:
                r = mid
            elif mid ** 2 < x:
                l = mid + 1
            else:
                return mid
            
        return l - 1
