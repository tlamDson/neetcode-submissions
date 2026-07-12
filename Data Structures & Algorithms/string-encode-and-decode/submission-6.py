class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#"  +i
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] !="#":
                j += 1
            val = int(s[i:j])
            res.append(str(s[j+1:j+1+val]))
            i = j + 1 + val
        return res
