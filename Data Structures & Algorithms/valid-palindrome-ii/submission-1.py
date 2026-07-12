class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # Slicing fixed to include the r-th character
                return self.isPalindrom(s[l+1:r+1]) or self.isPalindrom(s[l:r])
            l += 1
            r -= 1
        return True

    def isPalindrom(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]): # Fixed s[l] to s[r]
                r -= 1
            if s[l].lower() != s[r].lower(): 
                return False
            l += 1 
            r -= 1
        return True

    def alphaNum(self, c):
        return c.isalnum() # Pro-tip: Python has this built-in!