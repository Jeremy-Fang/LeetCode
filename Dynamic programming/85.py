class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not len(matrix) or not len(matrix[0]):
            return 0
        
        M = len(matrix)
        N = len(matrix[0])
        nums = [[int(matrix[i][j]) for j in range(N)] for i in range(M)]
        mx = 0
        
        def hist(row):
            nonlocal N
            mx_area = 0
            stack = []
            
            for i in range(N):
                while stack and row[stack[-1]] > row[i]:
                    top = row[stack.pop()]
                    area = top * i
                        
                    if stack:
                        area = top * (i-1-stack[-1])
                    mx_area = max(mx_area, area)
                stack.append(i)
            
            i += 1
            
            while stack:
                top = row[stack.pop()]
                area = top * i
                
                if stack:
                    area = top * (i-stack[-1]-1)
                mx_area = max(mx_area, area)
            
            return mx_area
        
        for i in range(M):
            if i == 0:
                mx = hist(nums[i])
            else:
                for j in range(N):
                    if nums[i][j]:
                        nums[i][j] += nums[i-1][j]
                mx = max(mx, hist(nums[i]))
                
            
        return mx
                    
        
