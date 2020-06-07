class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0 for i in range(2 * n)]
        list_odd_x = nums[0:n][0::2]
        list_odd_y = nums[n:2*n][0::2]
        list_even_x = nums[0:n][1::2]
        list_even_y = nums[n:2*n][1::2]
        
        for i in range(2 * n):
            if i % 4 == 0:
                res[i] = list_odd_x[i//4]
            if i % 4 == 1:
                res[i] = list_odd_y[i//4]
            if i % 4 == 2:
                res[i] = list_even_x[i//4]
            if i % 4 == 3:
                res[i] = list_even_y[i//4]
            
        return res
