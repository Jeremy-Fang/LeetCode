class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        count = 0
        N = len(tiles)
        maxes = collections.defaultdict(int)
        
        for tile in tiles: # get num of each tile
            maxes[tile] += 1
            
        def backtrack(curr_string, curr_map):
            nonlocal maxes
            nonlocal count
            nonlocal N
            if len(curr_string) == N:
                return
            
            for key in maxes.keys():
                if curr_map[key] < maxes[key]:
                    curr_map[key] += 1
                    count += 1
                    backtrack(curr_string + key, curr_map)
                    curr_map[key] -= 1
                    
        backtrack("", collections.defaultdict(int))
        
        return count
