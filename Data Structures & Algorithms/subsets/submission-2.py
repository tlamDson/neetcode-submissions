from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.n = len(nums)
        self.k = 2 # Chỉ có 2 lựa chọn: 0 (Không lấy) hoặc 1 (Lấy)
        
        self.A = [-1] * self.n 
        self.solutions = []
        
        self.backtrack(0)
        return self.solutions

    def backtrack(self, i):
        # Base case: Đã điền xong N ô
        if i == self.n:
            # Chuyển đổi mảng trạng thái (A) thành tập con thực tế
            current_subset = []
            for index in range(self.n):
                if self.A[index] == 1: # Nếu trạng thái là 1 thì lấy phần tử đó
                    current_subset.append(self.nums[index])
            
            self.solutions.append(current_subset)
            return

        # Đệ quy: Thử điền 0 và 1 vào ô thứ i
        for v in range(self.k):
            self.A[i] = v          # CHOOSE
            self.backtrack(i + 1)  # EXPLORE
            self.A[i] = -1         # UN-CHOOSE