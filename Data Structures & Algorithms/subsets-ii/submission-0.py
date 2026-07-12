class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        print(nums)
        self.A = [-1] * n
        self.subsets = []

        self.backtrack(0, n, 2, nums)

        return self.subsets
    def backtrack(self, i: int, n: int, k: int, nums: List[int]):
        # base case
      
        if i == n:
            subset = []
            for j in range(n):
                if self.A[j] == 0:
                    continue
                elif self.A[j] == 1:
                    subset.append(nums[j])
            self.subsets.append(subset)
            return
        
        # recursion
        # first i-th elements, build the (i+1)-th element, means A[i]
        for v in range(k):
                        
            self.A[i] = v
            if i > 0 and nums[i] == nums[i-1] and v == 1 and self.A[i-1] == 0 :
                continue
            self.backtrack(i + 1, n, k, nums)
            self.A[i] = -1
  
    





        