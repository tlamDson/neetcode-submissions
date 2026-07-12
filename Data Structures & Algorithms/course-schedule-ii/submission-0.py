from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(numCourses)}
        indegree = [0]*numCourses

        for t, p in prerequisites:
            adj[p].append(t)
            indegree[t] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        res = []
        count = 0
        while q:
            course = q.popleft()
            res.append(course)
            count += 1
            for next_course in adj[course]:
                indegree[next_course] -=1
                if indegree[next_course] == 0:
                    q.append(next_course)
        if count != numCourses:
            return []
        else: 
            return res


        
        