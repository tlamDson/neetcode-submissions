class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
            
        n = len(s)
        # Thay vì mảng dp, ta dùng 2 biến đại diện cho dp[i-2] và dp[i-1]
        prev2 = 1  # Tương đương dp[0]
        prev1 = 1  # Tương đương dp[1]
        
        for i in range(2, n + 1):
            current = 0
            
            # 1. Kiểm tra xem ký tự đơn lẻ có hợp lệ không
            one_digit = int(s[i-1 : i])
            if 1 <= one_digit <= 9:
                current += prev1
                
            # 2. Kiểm tra xem cặp 2 ký tự có hợp lệ không
            two_digits = int(s[i-2 : i])
            if 10 <= two_digits <= 26:
                current += prev2
                
            # Cập nhật trạng thái cho bước tiếp theo
            prev2 = prev1
            prev1 = current
            
            # Nếu tại một vị trí mà không có cách giải mã nào, dừng sớm trả về 0
            if prev1 == 0:
                return 0
                
        return prev1