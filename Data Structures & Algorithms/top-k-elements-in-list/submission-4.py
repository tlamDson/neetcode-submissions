from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        res = []
        # most_common(k) trả về list gồm k tuple (value, freq) lớn nhất
        for item in count.most_common(k):
            res.append(item[0])
        return res

                