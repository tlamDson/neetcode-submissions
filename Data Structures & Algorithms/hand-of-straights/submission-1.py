from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: 
            return False
        
        counts = Counter(hand)
        # Sort keys một lần duy nhất
        sorted_keys = sorted(counts.keys())
        
        for num in sorted_keys:
            # Nếu số này còn xuất hiện, ta bắt đầu tạo nhóm từ nó
            while counts[num] > 0:
                # Thử tạo một nhóm có độ dài groupSize
                for i in range(num, num + groupSize):
                    if counts[i] == 0:
                        return False # Không đủ lá bài để tạo nhóm liên tiếp
                    counts[i] -= 1
        
        return True