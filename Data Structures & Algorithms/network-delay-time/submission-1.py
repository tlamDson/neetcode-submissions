import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. Xây dựng danh sách kề (Adjacency List)
        # adj[u] sẽ lưu danh sách các cặp (v, weight)
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        print(adj)
        # 2. Khởi tạo bảng lưu thời gian ngắn nhất đến từng nút
        # Ban đầu mọi nút đều là vô cùng (float('inf')), nút gốc k là 0
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
        
        # 3. Khởi tạo Min-Heap với phần tử đầu tiên: (thời_gian, nút)
        # Heap luôn ưu tiên thằng có thời_gian nhỏ nhất lên đầu
        min_heap = [(0, k)]
        
        # Tập hợp dùng để đánh dấu các nút đã tìm được đường ngắn nhất tuyệt đối
        visited = set()
        
        # 4. Vòng lặp Dijkstra
        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            # Nếu nút này đã được tối ưu trước đó rồi thì bỏ qua (Bẫy trùng lặp)
            if node in visited:
                continue
                
            # Đánh dấu nút này đã xử lý xong hoàn toàn
            visited.add(node)
            
            # Duyệt qua các hàng xóm của nút hiện tại
            for neighbor, weight in adj[node]:
                # Nếu hàng xóm đã tối ưu rồi thì không cần sờ vào nữa
                if neighbor in visited:
                    continue
                    
                # Tính thời gian mới nếu đi qua nút hiện tại để đến hàng xóm
                new_time = time + weight
                
                # Nếu con đường mới này nhanh hơn con đường cũ từng ghi nhận
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    # Nạp con đường mới này vào Heap để tiếp tục mở rộng
                    heapq.heappush(min_heap, (new_time, neighbor))
            print(min_heap)
                    
        # 5. Kiểm tra kết quả cuối cùng
        # Nếu số nút đã tối ưu bằng đúng n, nghĩa là tín hiệu đã lan tới toàn mạng
        if len(visited) == n:
            # Thời gian để toàn mạng nhận được đồ là thời gian của nút nhận muộn nhất
            return max(dist.values())
        else:
            # Có nút bị cô lập, tín hiệu không tới được
            return -1