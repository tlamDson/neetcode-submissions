class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1),len(s2)

        if n1 > n2 : 
            return False

        s1_count = [0]*26
        s2_count = [0]*26
        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        for i in range(n1,n2):
            if s1_count == s2_count :
                return True
            
            new_idx = ord(s2[i]) - ord('a')
            s2_count[new_idx] += 1

            old_idx = ord(s2[i-n1]) - ord('a')
            s2_count[old_idx] -=1 
        
        return s1_count == s2_count

       