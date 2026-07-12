from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        count = 0
        current = 0
        for num in nums:
            current += num
            needed = current - k
            count += prefix_sum[needed]
            prefix_sum[current] += 1
        return count

        
        

       
            
            

            
        