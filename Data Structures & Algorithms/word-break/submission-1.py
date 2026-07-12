class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # ý tưởng của bìa này là tạo thành một cái dict để độ truy cập là O(1)
        word_set = set(wordDict)
        dp = [False]*(len(s) + 1)
        dp[0] = True
        print(dp)
        for i in range(1,len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
        return dp[-1]



        