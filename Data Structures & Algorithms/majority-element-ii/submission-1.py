class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Step 1: Find potential candidates
        cand1, cand2, count1, count2 = None, None, 0, 0
        
        for n in nums:
            if cand1 == n:
                count1 += 1
            elif cand2 == n:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Verify candidates (Boyer-Moore only guarantees candidates, not that they meet the threshold)
        res = []
        for cand in [cand1, cand2]:
            if cand is not None and nums.count(cand) > len(nums) // 3:
                res.append(cand)
                
        return res