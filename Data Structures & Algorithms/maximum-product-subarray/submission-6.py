class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # giống bài max sum 
        # glob_max = max(glob_max, curr_sum)
        # curr_sum = max(curr_sum + nums[i],nums[i])
        # case của bài này là 3 biến 
        #glob_max track max
        # curr_max lấy max hiện tại
        # curr_min lấy min vì array nhân âm vẫn có thể lớn nhất
        glob_max = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        for i in range(1,len(nums)):
            curr_num = nums[i]
            prev_max = curr_max
            prev_min = curr_min
            curr_min = min(curr_num, prev_max*curr_num, prev_min*curr_num)
            curr_max = max(curr_num, prev_max*curr_num, prev_min*curr_num)
            glob_max = max(glob_max, curr_max, curr_min)
            print(curr_max, curr_min, glob_max)
        return glob_max
        