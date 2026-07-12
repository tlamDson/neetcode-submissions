class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k :
            return 0
        res = 0
        for i in range(len(arr) - k + 1):
            avg = sum(arr[i:i+k]) / k
            print(arr[i:i+k],avg)
            if avg >= threshold:
                res +=1
        return res
                

        