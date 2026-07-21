from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(None)
        def dfs(i: int) -> int:
            # Base case: đi hết chuỗi thành công -> tìm được 1 cách decode
            if i == len(s):
                return 1
            
            # Số '0' không thể đứng đầu một mã decode
            if s[i] == '0':
                return 0
            
            # TH1: Decode 1 chữ số tại s[i]
            ans = dfs(i + 1)
            
            # TH2: Decode 2 chữ số s[i:i+2] (nếu từ 10 đến 26)
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ans += dfs(i + 2)
                
            return ans

        return dfs(0)