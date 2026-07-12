class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        def palindrome(l,r):
            num_pa = 0
            while l >= 0 and r < n and s[l] == s[r]:
                l -=1 
                r +=1
                num_pa += 1
            return num_pa
        res = 0
        for i in range(n):
            res += (palindrome(i,i) + palindrome(i,i+1))
        return res
            
            
