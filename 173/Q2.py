class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        v = sorted([i for i in sorted(restaurants, key=lambda i: i[0], reverse=True) \
                    if (not veganFriendly or (veganFriendly and i[2] == veganFriendly)) \
                    and i[3] <= maxPrice and i[4] <= maxDistance], \
                   key=lambda i: i[1], reverse=True)
        
        return [i[0] for i in v]
