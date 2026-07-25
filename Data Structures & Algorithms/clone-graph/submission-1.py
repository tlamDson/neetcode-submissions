from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None

        # Khởi tạo map và queue với nút gốc
        old_to_new = {node: Node(node.val)}
        q = deque([node])

        while q:
            curr_node = q.popleft()

            # Duyệt qua từng hàng xóm của nút cũ
            for neighbor in curr_node.neighbors:
                # 1. Nếu chưa gặp neighbor này bao giờ -> Tạo bản sao & đẩy vào queue
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                
                # 2. Nối bản sao của curr_node với bản sao của neighbor
                old_to_new[curr_node].neighbors.append(old_to_new[neighbor])

        # Trả về bản sao của nút gốc ban đầu
        return old_to_new[node]