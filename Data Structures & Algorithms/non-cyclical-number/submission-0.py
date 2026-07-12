class Solution:
    def isHappy(self, n: int) -> bool:
        def getNextNumber(n: int) -> int:
            total_sum = 0
            while n > 0:
                digit = n % 10
                total_sum += digit ** 2  # Hoặc viết: digit * digit
                n //= 10
            return total_sum
        my_dict = set()
        while n:
            n = getNextNumber(n)
            if n == 1: return True
            if n in my_dict:
                return False
            else: 
                my_dict.add(n)
        return False
        
        

        