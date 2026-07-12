class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        prefix  = [0]*len(nums)

        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]

        def getSum(l,r):
            if l == 0:
                return prefix[r]
            return prefix[r] - prefix[l-1]
        ans = 1
        for r in range(n):
            low = 0
            high = r
            best_l = r

            while low <= high:
                mid = (low + high) // 2
                actual_sum = getSum(mid, r)
                target_sum = ( r - mid + 1)*nums[r]
                if target_sum - actual_sum <= k:
                    best_l = mid
                    high = mid - 1
                else:
                    low = mid + 1
            ans = max(ans, r - best_l + 1)
        return ans
        
                    

