class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # Mặt nạ giữ lại đúng 32 bit cuối
        
        while b & mask:  # Vòng lặp dừng khi b không còn bit nào nằm trong phạm vi 32 bit
            carry = (a & b) << 1
            a = (a ^ b) & mask      # Ép tổng không nhớ về 32-bit ngay lập tức
            b = carry & mask        # Ép số nhớ về 32-bit ngay lập tức
            
        # Xử lý trả về số âm/dương chuẩn 32-bit cho Python
        # 0x7FFFFFFF là số dương lớn nhất của hệ 32-bit signed integer
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)