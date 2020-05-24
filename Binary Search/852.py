class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l = 1
        r = len(A)-2
        
        while l <= r:
            mid = (l+r)//2
            if A[mid-1] < A[mid] > A[mid+1]:
                return mid
            if A[mid-1] < A[mid] < A[mid+1]: #increasing
                l = mid + 1
            else: #decreasing
                r = mid - 1
        
        return l
                
