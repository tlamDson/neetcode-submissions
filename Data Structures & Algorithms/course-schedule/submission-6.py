from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj ={ i: [] for i in range(numCourses)}

        indegree = [0]*numCourses
        for t, p in prerequisites:
            adj[p].append(t)
            indegree[t] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        count = 0
        while q:
            course = q.popleft()
            count += 1
            for next_course in adj[course]:
                indegree[next_course] -=1
                if indegree[next_course] == 0:
                    q.append(next_course)
        return count == numCourses

        
        


        