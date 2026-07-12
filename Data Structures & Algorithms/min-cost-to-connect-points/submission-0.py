from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # 1. Khởi tạo cấu trúc Union-Find
        # - Mảng parent: ban đầu mỗi điểm là gốc của chính nó.
        # - Mảng rank (hoặc size): để tối ưu hóa khi gộp (Union by Rank/Size).
        parent = [i for i in range(len(points) + 1)]
        rank = [0 for i in range(len(points) + 1)]
        
        # 2. Tạo danh sách tất cả các cạnh có thể có
        # - Dùng 2 vòng lặp for để duyệt mọi cặp (i, j).
        # - Tính khoảng cách Manhattan: abs(x1 - x2) + abs(y1 - y2).
        # - Lưu vào một danh sách dạng: (chi phí, điểm_i, điểm_j).
        adj = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj.append((distance, i, j))

        
        # 3. Sắp xếp các cạnh theo chi phí tăng dần
        # - Đây là bước quan trọng nhất của thuật toán Kruskal.
        adj.sort()        
        # Hàm find: Tìm gốc của một node (nên có Path Compression)
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        # Hàm union: Hợp nhất hai tập hợp
        # Trả về True nếu gộp thành công, False nếu đã chung gốc
        def union(i, j):
            rx, ry = find(i), find(j)
            if rx == ry:
                return False
            if rank[rx] > rank[ry]:
                parent[ry] = rx
            elif rank[rx] < rank[ry]:
                parent[rx] = ry
            else:
                parent[rx] = ry
                rank[ry] += 1
            return True
            
        min_cost = 0
        edges_count = 0
        for cost, u, v in adj:
            if union(u,v):
                min_cost += cost
                edges_count += 1
            if edges_count == n - 1:
                break
        return min_cost