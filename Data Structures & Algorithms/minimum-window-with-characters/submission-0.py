class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        dict_t = Counter(t)
        required = len(dict_t) # Số lượng ký tự độc nhất cần có
        
        l, r = 0, 0
        formed = 0 # Số lượng ký tự độc nhất đã thỏa mãn số lượng yêu cầu
        window_counts = {}
        
        # Kết quả: (độ dài, l, r)
        ans = float("inf"), None, None
        
        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            
            # Khi đã thỏa mãn, bắt đầu thu hẹp l
            while l <= r and formed == required:
                char = s[l]
                
                # Cập nhật kết quả tốt nhất
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # Thu hẹp cửa sổ
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                l += 1
            
            r += 1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]