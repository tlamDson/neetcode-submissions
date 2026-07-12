class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_map = {0:-1}
        current_sum = 0

        for i, n in enumerate(nums):
            current_sum += n
            remainder = current_sum % k 
            if remainder in rem_map:
                if i -rem_map[remainder] >= 2:
                    return True
            else:
                rem_map[remainder]  = i
        return False