class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 1. Edge case: Nếu mảng rỗng thì không có xu nào
        if not nums: 
            return 0
        
        # Lưu lại số lượng bóng thực tế ban đầu
        n = len(nums)
        
        # 2. Bọc hai số 1 ở đầu và cuối mảng
        nums.append(1)
        nums.insert(0, 1)
        
        # 3. Khởi tạo bảng dp 2 chiều kích thước (n+2) x (n+2) toàn số 0
        # dp[l][r] sẽ lưu số xu lớn nhất khi bắn hết bóng từ index l đến r
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        # 4. Vòng lặp 1: Duyệt theo ĐỘ DÀI của đoạn bóng (từ 1 quả đến n quả)
        for length in range(1, n + 1):
            
            # Vòng lặp 2: Xác định điểm đầu l của đoạn bóng
            for l in range(1, n - length + 2):
                # Điểm cuối r tự động tính dựa theo điểm đầu và độ dài
                r = l + length - 1
                
                # Vòng lặp 3: Thử từng quả bóng k nằm giữa l và r làm quả bóng nổ CUỐI CÙNG
                for k in range(l, r + 1):
                    # Tiền ăn được từ quả k = biên trái ngoài * quả k * biên phải ngoài
                    coins = nums[l - 1] * nums[k] * nums[r + 1]
                    
                    # Cộng thêm số tiền tối ưu đã giải được từ cụm trái và cụm phải trước đó
                    coins += dp[l][k - 1] + dp[k + 1][r]
                    
                    # Cập nhật kết quả kỷ lục vào ô bảng hiện tại
                    dp[l][r] = max(dp[l][r], coins)
        return dp[1][n]
                    
