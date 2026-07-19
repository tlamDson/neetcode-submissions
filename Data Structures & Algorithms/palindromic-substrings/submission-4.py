class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        if n == 1 : return 1
        def countPalindrome(start, end):
            count = 0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -=1
                end +=1
                count += 1
            return count
        res = 0
        for i in range(len(s)):
            odd_palindrome = countPalindrome(i,i)
            even_palindrome = countPalindrome(i,i + 1)
            res += odd_palindrome + even_palindrome
        return res



        