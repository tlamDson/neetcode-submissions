from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count_k = sorted(count.items(), key = lambda item:item[1], reverse = True)
        res = []
        
        for value, freq in count_k:
            res.append(value)
        return res[0:k]

        
        
        # list 
        # runtime o(nlogn) 
        # space (o(k))
        # dungf counter sau do sorted sau do return k cai dau tien
        