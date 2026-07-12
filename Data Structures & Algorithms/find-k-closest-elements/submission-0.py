class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if k > n:
            return []
        if k ==n : 
            return arr
        res = []
        l = 0
        r = 0
        while r - l < k:
            res.append(arr[r])
            r += 1
        while r < n:
            if abs(arr[r] - x) <  abs(arr[l] - x) or (abs(arr[r] - x) <  abs(arr[l] - x) and arr[r] < arr[l]):
                res.append(arr[r])
                res.pop(0)
                l += 1
            r += 1
        return res

