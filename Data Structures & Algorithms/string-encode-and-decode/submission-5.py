class Solution:
    # runtime is o(n) with n is the lenght of the list+
    # space complexity is o(m+n) with n is the number of strings and m the sum of lengths of all str
    # the string can be special character how can we differentiate them 
    # # with the lenght of if after that right
    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + '*' + string  
        print(res)          
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        curr = 0
        while i < len(s):
            if s[i] == "*":
                length = int(s[curr:i])
                res.append(s[i+1:i + length+1])
                i += length + 1
                curr = i
            i += 1
        return res
