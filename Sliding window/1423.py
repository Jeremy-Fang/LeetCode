class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        x = cardPoints[0:k][::-1] + cardPoints[len(cardPoints)-k:][::-1]
        l = 0
        ma = s = sum(x[0:k])
        
        
        for r in range(k, len(x)):
            s += x[r] - x[r-k]
            ma = max(ma, s)
            
        return ma
            
