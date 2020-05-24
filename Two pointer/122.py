class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = None
        res = 0
        
        for i in range(len(prices) - 1):
            if mi == None:
                mi = i
            else:
                if prices[i] < prices[mi]:
                    mi = i
                elif prices[i] > prices[i+1]:
                    res += prices[i] - prices[mi]
                    mi = None
                    
        if mi != None:
            res += max(prices[-1] - prices[mi], 0)
            
        return res
