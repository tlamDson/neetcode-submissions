class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        self.A = [-1]*n
        self.subsets = []
        self.backtrack(0,n,2,candidates,target,0)
        return self.subsets

    def backtrack(self, i :int, n : int, k : int, candidates : List[int], target: int, currentSum : int) -> List[List[int]]:
        if currentSum == target:
            subset = []
            for j in range(i):
                if self.A[j] == 1:
                    subset.append(candidates[j])
            self.subsets.append(subset)
            return

        if i == n or currentSum > target:
            return
        for v in range(k):
            if i == 1 and currentSum > target:
                continue
            if i > 0 and candidates[i] == candidates[i-1] and v == 1 and self.A[i-1] == 0:
                continue
            self.A[i] = v
            newSum = currentSum + candidates[i] if v == 1 else currentSum
            self.backtrack(i + 1,n,k,candidates,target,newSum)
            self.A[i] = -1