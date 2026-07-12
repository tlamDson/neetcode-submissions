import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. Đếm tần suất xuất hiện của từng tác vụ
        # Ví dụ: {'A': 3, 'B': 3}
        counts = Counter(tasks)
        
        # 2. Đẩy tần suất vào Max-Heap (bằng cách nhân -1)
        # Ta chỉ cần quan tâm đến số lượng (tần suất), không cần quan tâm ký tự đó là gì
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        # Queue này đóng vai trò là "Khu vực làm nguội" (Cool-down list)
        # Lưu các cặp: (tần_suất_còn_lại, thời_gian_được_phép_quay_lại_heap)
        cooldown_queue = deque()
        
        # 3. Vòng lặp mô phỏng từng đơn vị thời gian
        while max_heap or cooldown_queue:
            time += 1 # Thời gian trôi đi 1 đơn vị
            
            # Kịch bản A: Nếu heap còn tác vụ, bốc thằng nhiều nhất ra chạy
            if max_heap:
                # bốc ra số âm (ví dụ: -3), cộng 1 để giảm số lượng còn lại (thành -2)
                cnt = heapq.heappop(max_heap) + 1
                
                # Nếu tác vụ này vẫn còn lượt chạy (cnt khác 0)
                if cnt != 0:
                    # Đưa vào khu vực làm nguội. 
                    # Nó phải đợi đến thời điểm: thời_gian_hiện_tại + n mới được ra ngoài
                    cooldown_queue.append((cnt, time + n))
            
            # Kịch bản B: Kiểm tra xem có tác vụ nào ở khu làm nguội đã hết án phạt chưa
            if cooldown_queue and cooldown_queue[0][1] == time:
                # Đủ thời gian làm nguội, bốc ra khỏi queue và nạp trả lại vào Max-Heap
                cnt, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, cnt)
                
        return time