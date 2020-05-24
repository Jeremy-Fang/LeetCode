class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def binarySearch(a):
            l = 0
            r = len(a)-1
            
            while l <= r:
                m = (l + r) // 2
                if a[m] >= 0:
                    l = m + 1
                else:
                    r = m - 1
            
            return len(a) - l
        
        res = 0
        N = len(grid[0])
        
        for row in grid:
            res += binarySearch(row)
            
        return res
