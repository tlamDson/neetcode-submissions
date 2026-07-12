from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p and s: return True
        @lru_cache(None)
        def dfs(i,j):
            # base case
            if j == len(p):
                if i == len(s): 
                    return True
                else:
                    return False
            if j + 1 < len(p) and p[j + 1] == '*':
                exclude = dfs(i , j  + 2)
                if i < len(s) and  (s[i] == p[j] or p[j] == '.'):
                    include = dfs(i + 1,j)
                else: 
                    include = False
                return include or exclude
            if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                return dfs(i + 1, j + 1)
            return False
            
        return dfs(0,0)

            
        

        
        