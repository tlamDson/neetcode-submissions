class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # chạy ngược từ dưới lên 5 + 1 thì = 6 nếu khác không thì thôi 
        # vòng while là while carry != 0
        # ngay khi mà carry = 0 thì return 
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if carry == 0: return digits
            if digits[i] < 9:
                digits[i] += carry
                carry -=1
            else:
                digits[i] = 0
                carry = 1
        if carry == 1:
            digits.insert(0,1)
        
        return digits


            

        
        