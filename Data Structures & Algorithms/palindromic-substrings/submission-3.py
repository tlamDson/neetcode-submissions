class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindrome(start, end, s):
            count = 0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -=1
                end +=1
                count += 1
            return count
        res = 0
        for i in range(len(s)):
            odd_palindrome = countPalindrome(i,i,s)
            even_palindrome = countPalindrome(i,i + 1,s)
            res += odd_palindrome + even_palindrome
        return res



        