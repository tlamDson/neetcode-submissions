class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start_index,path,k):
            if len(path) == k:
                res.append(list(path))
                return 
            for j in range(start_index,n + 1):
                path.append(j)
                backtrack(j + 1, path,k)
                path.pop()
        backtrack(1,[],k)
        return res


        