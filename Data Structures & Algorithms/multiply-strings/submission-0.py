class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
            
        # Mảng chứa kết quả trung gian, độ dài tối đa bằng tổng độ dài 2 chuỗi
        res = [0] * (len(num1) + len(num2))
        
        # Duyệt ngược từ cuối lên của cả 2 chuỗi
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Chuyển ký tự thành số bằng ord()
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                # Nhân 2 chữ số và cộng thêm giá trị đang có sẵn ở ô kết quả hiện tại
                mul = digit1 * digit2 + res[i + j + 1]
                
                # Cập nhật hàng đơn vị tại vị trí hiện tại (i + j + 1)
                res[i + j + 1] = mul % 10
                
                # Cộng dồn phần nhớ vào hàng chục phía trước (i + j)
                res[i + j] += mul // 10
                
        # Chuyển mảng số thành chuỗi, bỏ các số 0 thừa ở đầu nếu có
        result_str = "".join(str(digit) for digit in res)
        
        # Lstrip để xóa số 0 ở đầu (ví dụ "0123" -> "123")
        return result_str.lstrip('0')
