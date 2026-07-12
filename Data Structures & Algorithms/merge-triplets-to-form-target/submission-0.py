class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # nếu mà không match thì sao
        #  2,5,6  và 1,4,4 = 2,5,6
        # if  bé hơn thì sao thì chuyển qua dùng thằng 5,7,5
        # chỉ được chạy 1 lần qua cả array làm sao mà sô hêt possible outcomes
        # dùng greedy ngay lần chạy đầu tiên khogon được thì lấy cái match nhiều nhất'
        # 2,5,6 match thuần greedy luôn
        # brute force sẽ là thử hết các cặp và là o(n^2)
        # determine cái có khả năng nhiều nhất
        # bỏ qua triplet có value > target
        max_so_far = [0,0,0]
        
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            max_so_far[0] = max(max_so_far[0],triplet[0])
            max_so_far[1] = max(max_so_far[1],triplet[1])
            max_so_far[2] = max(max_so_far[2],triplet[2])
            if (max_so_far[0] == target[0]) and (max_so_far[1] == target[1]) and (max_so_far[2] == target[2]):
                return True
            
        return False

        