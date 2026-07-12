class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                result = [l+1,r+1]
                break
            elif total < target:
                l += 1
            else:
                r -=1
        return [] if not result else result
        
       