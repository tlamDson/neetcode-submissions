class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        isVisited = [False]*len(s)
        def isPalindrome(string):
            l,r = 0,len(string) - 1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -=1
            return True
        def backtrack(path,start):
            if start == len(s):
                res.append(list(path))
                return 
            for j in range(start,len(s)):
                sub_string = s[start:j+1]
                if not isPalindrome(sub_string):
                    continue
                path.append(sub_string)
                backtrack(path,j + 1)
                path.pop()
        backtrack([],0)
        return res


            


            

            