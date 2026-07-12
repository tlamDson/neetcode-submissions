class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mặt nạ 32-bit (chứa 32 bit 1) để giới hạn phạm vi số nguyên trong Python
        # Vì Python hỗ trợ số nguyên vô hạn, ta cần mask này để giả lập cơ chế tràn số 32-bit
        mask = 0xFFFFFFFF
        
        # Vòng lặp chạy liên tục cho đến khi không còn bit nhớ (b đóng vai trò là carry)
        while b != 0:
            # 1. Tính tổng không nhớ bằng phép XOR
            # & mask để đảm bảo kết quả luôn nằm trong giới hạn 32-bit
            tong_khong_nho = (a ^ b) & mask
            
            # 2. Tính bit nhớ bằng phép AND, sau đó dịch trái 1 đơn vị
            # Phải dịch trái vì bit nhớ sẽ được cộng vào hàng kế tiếp bên trái
            carry = ((a & b) << 1) & mask
            
            # 3. Cập nhật lại a và b cho lượt lặp tiếp theo
            a = tong_khong_nho
            b = carry
            
        # XỬ LÝ SỐ ÂM SAU VÒNG LẶP (Đặc trưng của Python):
        # Nếu bit cao nhất (bit thứ 31) là 1, nghĩa là đây là một số âm dưới dạng bù 2
        if a > 0x7FFFFFFF:
            return ~(a ^ mask)
            
        return a