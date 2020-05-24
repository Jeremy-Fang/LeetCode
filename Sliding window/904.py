class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        l = r = 0
        one = two = -1
        last_one = last_two = -1
        ma = 0
        L = len(tree)
        
        while r < L:
            if tree[r] != one:
                if one == -1:
                    one = tree[r]
                else:
                    if tree[r] != two:
                        if two == -1:
                            two = tree[r]
                        else:
                            l = min(last_one, last_two) + 1
                            if last_one < last_two:
                                one = two
                                last_one = last_two
                            two = tree[r]
                            last_two = r
            if tree[r] == one:
                last_one = r
            if tree[r] == two:
                last_two = r
                
            r += 1
            ma = max(ma, r - l)
            
        return ma
