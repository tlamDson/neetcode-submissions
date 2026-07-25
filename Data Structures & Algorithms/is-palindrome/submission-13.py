class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for s in s:
            if s.isalnum():
                new_str += s.lower()
        l, r = 0 , len(new_str) - 1
        while l <= r:
            if new_str[l] != new_str[r]:
                return False
            l += 1
            r -=1
        return True
    
        