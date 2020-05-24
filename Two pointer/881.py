class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        l = 0
        r = L = len(people) - 1
        res = 0
        
        
        while l <= r:
            if people[r] + people[l] <= limit:
                l += 1
                r -=1
            else:
                if people[r] > people[l]:
                    r -= 1
                else:
                    l += 1
            res += 1
            
        return res
