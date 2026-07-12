class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = [0]*26
        for s in s1:
            index = ord(s) - ord('a')
            s1_count[index] += 1
        n = len(s1)
        
        for i in range(len(s2) - n + 1):
            current = s2[i:i+n]
            s2_count = [0]*26
            for s in current:
                index = ord(s) - ord('a')
                s2_count[index] += 1
                print(s2_count)
            if s1_count == s2_count:
                return True
        return False

        