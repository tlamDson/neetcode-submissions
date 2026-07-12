class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        
        # Edge case: s1 cannot be a permutation of s2 if it's longer
        if n1 > n2:
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        # 1. "Priming" the window: Fill s1_count AND the first window of s2
        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # 2. Slide the window across s2
        # We start from index n1 because we already processed 0 to n1-1
        for i in range(n1, n2):
            # Check if the current window is a match
            if s1_count == s2_count:
                return True
            
            # Slide logic:
            # ADD the character entering from the right
            s2_count[ord(s2[i]) - ord('a')] += 1
            
            # REMOVE the character exiting from the left
            # The character to remove is exactly n1 steps behind our current index i
            s2_count[ord(s2[i - n1]) - ord('a')] -= 1

        # 3. Final check for the very last window
        return s1_count == s2_count