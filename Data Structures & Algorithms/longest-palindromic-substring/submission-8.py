class Solution:
    def longestPalindrome(self, s: str) -> str:
        # bài này dùng manacher
        # hoặc dfs tìm nhưng nên chèn thêm cái gì đó vào để cchayj tốt hơn vì sẽ out of range
        # chèn # vào
        # nếu khác thì đếm 
        # còn nếu dài nhất thì là cho thêm vào thôi
        lmax, rmax = 0,0
        n = len(s)
        if len(s) == 0: return ""
        if len(s) == 1: return s
        def palindrome(l,r,n):
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -=1
                r += 1
            return l + 1, r -1
        for i in range(n):
            l1, r1 = palindrome(i,i,n)
            l2, r2 = palindrome(i,i+1,n)
            if r1 - l1 > rmax - lmax:
                rmax, lmax = r1, l1
            if r2 - l2 > rmax - lmax:
                rmax, lmax = r2 ,l2
            if rmax - lmax + 1 == len(s):
                return s
        return s[lmax:rmax + 1]

                    
        