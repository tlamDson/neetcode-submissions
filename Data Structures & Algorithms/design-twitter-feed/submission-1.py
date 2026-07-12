from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0
        # followMap = { 1 : (2), 2 : (1)}
        # tweetMap = { 1 : [(1,10)], 2 : [(2,20)]}
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweetMap[userId].append((self.count, tweetId))
    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        res = []
        
        # Gom chính mình và những người mình follow vào chung một tập hợp
        user_ids = set(self.followMap[userId])
        user_ids.add(userId)
        
        for uid in user_ids:
            if uid in self.tweetMap and self.tweetMap[uid]:
                # Lấy chỉ số của bài đăng cuối cùng (mới nhất)
                last_idx = len(self.tweetMap[uid]) - 1
                count, tweetId = self.tweetMap[uid][last_idx]
                
                # Nạp vào Heap: (-count, tweetId, uid, chỉ_số_bài_kế_tiếp)
                max_heap.append((-count, tweetId, uid, last_idx - 1))
        
        # Chỉ heapify tối đa K phần tử (K là số người mình follow, rất nhỏ!)
        heapq.heapify(max_heap)
        
        remain = 10
        while remain > 0 and max_heap:
            remain -= 1
            neg_count, tweetId, uid, next_idx = heapq.heappop(max_heap)
            res.append(tweetId)
            
            # Nếu người vừa bị pop bài vẫn còn bài cũ hơn trong quá khứ
            if next_idx >= 0:
                count, next_tweetId = self.tweetMap[uid][next_idx]
                # Nạp duy nhất bài cũ hơn đó vào heap để thế chỗ
                heapq.heappush(max_heap, (-count, next_tweetId, uid, next_idx - 1))
                
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].discard(followeeId)
