from functools import lru_cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        isVisited = [False]*len(s)
        @lru_cache(None)
        def isPalindrome(start,end):
            l,r = start, end
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -=1
            return True
        def backtrack(path,start):
            if start == len(s):
                res.append(list(path))
                return 
            for j in range(start,len(s)):
                if isPalindrome(start,j):
                    path.append(s[start:j+1])
                    backtrack(path,j+1)
                    path.pop()
        backtrack([],0)
        return res


            


            

            