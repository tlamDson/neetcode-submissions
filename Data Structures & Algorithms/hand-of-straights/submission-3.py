from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        counts = Counter(hand)
        sorted_keys = sorted(counts.keys())
        for num in sorted_keys:
            while counts[num] > 0:
                for i in range(num, num + groupSize):
                    if counts[i] == 0:
                        return False
                    counts[i] -= 1
        return True