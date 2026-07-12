class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Khởi tạo tất cả bằng phần tử đầu tiên
        curr_max = nums[0]
        curr_min = nums[0]
        global_max = nums[0]
        
        # Bắt đầu duyệt từ phần tử thứ 2 (chỉ số 1)
        for i in range(1, len(nums)):
            num = nums[i]
            
            # Phải cất curr_max hiện tại (đóng vai trò là Max_cũ) vào một biến tạm
            temp_max = curr_max
            
            # Tính toán trạng thái mới cho bước i
            curr_max = max(num, temp_max * num, curr_min * num)
            curr_min = min(num, temp_max * num, curr_min * num)
            print(curr_max,curr_min)
            
            # So sánh với kỷ lục toàn cục
            global_max = max(global_max, curr_max)
            
        return global_max