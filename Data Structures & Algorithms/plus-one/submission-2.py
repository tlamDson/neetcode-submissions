class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # chạy ngược từ dưới lên 5 + 1 thì = 6 nếu khác không thì thôi 
        # vòng while là while carry != 0
        # ngay khi mà carry = 0 thì return 
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + digits


            

        
        