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
        print(self.tweetMap)
    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        
        for count, tweetId in self.tweetMap[userId]:
            max_heap.append((-count, tweetId))
        if self.followMap[userId] is not None:
            for follower in self.followMap[userId]:
                for count, tweetId in self.tweetMap[follower]:
                    max_heap.append((-count, tweetId))
        heapq.heapify(max_heap)
        res = []
        remain = 10
        while remain > 0 and max_heap:
            remain -= 1
            count, tweetId = heapq.heappop(max_heap)
            res.append(tweetId)
        return res


            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].discard(followeeId)
