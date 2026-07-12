class Solution:
    def isHappy(self, n: int) -> bool:
        def getNextNumber(n: int) -> int:
            total_sum = 0
            while n > 0:
                digit = n % 10
                total_sum += digit ** 2  # Hoặc viết: digit * digit
                n //= 10
            return total_sum
        seen_numbers = set()
        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = getNextNumber(n)
        return n == 1
        
        

        