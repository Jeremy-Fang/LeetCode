class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        N = len(arr)
        start = 0
        sum = 0
        track = [1e100] * N
        ans = 1e100
        mn = 1e100
        
        for end in range(N):
            sum += arr[end]
            
            while sum > target and start < end:
                mn = min(track[start], mn)
                sum -= arr[start]
                start += 1
                
            if sum == target:
                track[end] = min(track[end], end - start + 1)
                ans = min(ans, mn + end - start + 1)
                
        if ans == 1e100:
            return -1
        return ans
