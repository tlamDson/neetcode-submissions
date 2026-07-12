from collections import deque, defaultdict
from typing import List
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}
        in_degree = {char : 0 for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for neighbor in adj[curr]:
                in_degree[neighbor] -=1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        if len(result) < len(in_degree):
            return ""
        return "".join(result)

            
        