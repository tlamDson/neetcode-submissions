import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return x**2 + y**2

        max_heap = []
        
        for point in points:
            dist = distance(point[0], point[1])
            
            # Mẹo Max-Heap: Nhân thêm dấu trừ '-' vào tiêu chí so sánh (khoảng cách)
            # Ta lưu luôn cả cái `point` [x, y] vào Tuple để tí đỡ phải tra cứu theo chỉ số i
            heapq.heappush(max_heap, (-dist, point))
            
            # CHỐT CHẶN BỘ NHỚ: Nếu heap thừa người (> k), đuổi thằng xa nhất ra ngay lập tức
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        # Lúc này max_heap chỉ còn đúng k phần tử gần nhất
        # Trích xuất dữ liệu point ra khỏi Tuple để trả về kết quả
        res = []
        for dist,point in max_heap:
            res.append(point)
        return res