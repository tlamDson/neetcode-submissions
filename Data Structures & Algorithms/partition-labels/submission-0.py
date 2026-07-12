from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # tìm lần suất hiện cuối cùng của mỗi chữ cái'
        # cho một biến max_end
        # nếu mà đang chạy mà gặp cái khác thì tính max_end = max(max_end, chuỗi cuối cugnf của chữ cái kia)
        first_time = set()
        last_appear = defaultdict(int)
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in first_time:
                first_time.add(s[i])
                last_appear[s[i]] = i        
        max_reach = 0
        res = []
        length = 0
        for i in range(len(s)):
            last_appear_i = last_appear[s[i]]
            max_reach = max(max_reach,last_appear_i)
            length += 1
            if max_reach == i:
                res.append(length)
                length = 0
        return res
            



        
        