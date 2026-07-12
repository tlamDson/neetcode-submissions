from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        myDict = defaultdict(int)
        myDict[0] = 1
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            target = current_sum - k
            if target in myDict:
                count += myDict[target]
            myDict[current_sum] += 1
        return count
    
        
        

       
            
            

            
        