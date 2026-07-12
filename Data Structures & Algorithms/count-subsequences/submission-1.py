from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        dp = [[-1]*len(t) for _ in range(len(s))]

        def dfs(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = dfs(i + 1, j)
            if s[i] == t[j]:
                dp[i][j] += dfs(i + 1, j + 1)
            return dp[i][j]
        return dfs(0,0)

        