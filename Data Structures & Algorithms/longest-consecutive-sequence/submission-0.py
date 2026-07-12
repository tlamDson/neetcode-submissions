class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in num_set:
            if num - 1 not in num_set:
                start = num -1
                current = 0
                while start + 1 in num_set:
                    current += 1
                    start += 1
                res = max(res, current)
        return res
                
                        
                


        