class Solution:
    def backtrack(self, i :int, n :int, k :int, nums : List[int]):
        if i == n:
            subset = []
            for j in range(n):
                if self.A[j] == 0:
                    continue
                elif self.A[j] == 1:
                    subset.append(nums[j])
            self.subsets.append(subset)
            return
        
        for v in range(k):
            self.A[i] = v
            self.backtrack(i+1,n,k,nums)
            self.A[i] = -1
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.A = [-1]*n
        self.subsets = []
        self.backtrack(0,n,2,nums)
        return self.subsets
