class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Lưu chỉ số
        max_area = 0
        heights.append(0)  # Thêm phần tử chặn để xử lý nốt các thanh còn lại
        
        for i, h in enumerate(heights):
            # Khi gặp thanh thấp hơn, bắt đầu tính toán diện tích cho các thanh trong stack
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # Nếu stack rỗng, width là i; nếu không, width là khoảng cách giữa 2 biên
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
            
        return max_area

        