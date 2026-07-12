class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            string_s = Solution.countStrings(s)
            string_t = Solution.countStrings(t)
            print(string_s,string_t)
            if string_s.keys() == string_t.keys():
                return (string_s == string_t) 
        return False
        
    def countStrings(string):
        countString = {}
        for num in string:
            if num in countString:
                countString[num] += 1
            else:
                countString[num] = 1
        return dict(sorted(countString.items()))