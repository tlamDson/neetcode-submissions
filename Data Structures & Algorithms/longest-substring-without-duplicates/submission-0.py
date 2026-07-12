class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s : return 0 
        charSet = set()
        l = 0
        res = 0
        for i in range(len(s)):
            print(charSet)
            print(i)

            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1
                print(l)
            charSet.add(s[i])
            res = max(res, i - l + 1)
        return res
        
                