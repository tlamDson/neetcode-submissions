class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {} # char -> lastIdx
        for i, c in enumerate(s):
            lastIndex[c] = i
        res = []
        length = 0
        max_reach = 0
        for i, c in enumerate(s):
            length += 1
            max_reach = max(max_reach, lastIndex[c])
            if i == max_reach:
                res.append(length)
                length = 0
                max_reach = 0
        return res
        