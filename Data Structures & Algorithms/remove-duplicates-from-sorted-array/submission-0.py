class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        l = 0  # Con trỏ chốt chặn (số duy nhất cuối cùng tìm thấy)
        
        for r in range(1, len(nums)):  # r là con trỏ khám phá
            if nums[r] != nums[l]:     # Nếu tìm thấy một số mới khác với số tại l
                l += 1                 # Nhảy sang ô tiếp theo để chuẩn bị ghi
                nums[l] = nums[r]      # Ghi số mới đó vào
        
        return l + 1  # Vì l bắt đầu từ 0, nên số lượng phần tử là l + 1