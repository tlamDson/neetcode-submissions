class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, path, total):
            if total == target:
                res.append(path.copy())
                return 
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if total + candidates[j] > target:
                    return 
                path.append(candidates[j])
                backtrack(j + 1, path, total + candidates[j])
                path.pop()
        backtrack(0,[],0)
        return res
# 1,2,2,4,5,6,9
        