class Solution:
    def checkStraightLine(self, coord: List[List[int]]) -> bool:
        coord = sorted(coord, key=lambda i: i[0])
        slope = float('-inf')
        
        for i in range(len(coord) - 1):
            if slope == float('-inf'):
                if coord[i+1][0] == coord[i][0]:
                    slope = float('inf')
                else:
                    slope = (coord[i+1][1] - coord[i][1])/(coord[i+1][0] - coord[i][0])
            else:
                if coord[i+1][0] != coord[i][0]:
                    if (coord[i+1][1] - coord[i][1])/(coord[i+1][0] - coord[i][0]) != slope:
                        return False
                else:
                    if slope != float('inf'):
                        return False
        return True
