class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        h_cuts, v_cuts = [0] + sorted(horizontalCuts) + [h], [0] + sorted(verticalCuts) + [w] 
        
        max_width = 0
        max_height = 0
        
        for x in range(len(h_cuts) - 1):
            max_width = max(max_width, h_cuts[x+1] - h_cuts[x])
            
        for y in range(len(v_cuts) - 1):
            max_height = max(max_height, v_cuts[y+1] - v_cuts[y])
            
        return (max_width * max_height) % (10**9 + 7)
