class Solution:
    # hello/world/
    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            length = len(string)
            res += str(length) + '#' +  string 
        print(res)
        return res
            

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        curr = 0
        while i < len(s):
            if s[i] == '#':
                num = int(s[curr:i])
                string = ""
                for j in range(num):
                    i += 1
                    string += s[i]
                res.append(string)
                curr = i + 1
            i += 1
        return res