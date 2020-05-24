class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        
        if self.n == 0:
            return
        
        self.ps = [0] * self.n
        
        for i in range(self.n):
            if i == 0:
                self.ps[i] = nums[i]
            else:
                self.ps[i] = self.ps[i-1] + nums[i]
            
    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.ps[j]
        return self.ps[j] - self.ps[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
