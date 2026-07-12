class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def can_swim(time):
            # DFS trả về True nếu đi được từ (0,0) đến (n-1, n-1)
            visited = set()
            def dfs(r, c):
                if r == n - 1 and c == n - 1:
                    return True
                visited.add((r, c))
                
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] <= time:
                        if dfs(nr, nc):
                            return True
                return False
            
            return dfs(0, 0)

        # Binary Search để tìm 't' tối ưu
        low = grid[0][0]
        high = n * n - 1
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if can_swim(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans