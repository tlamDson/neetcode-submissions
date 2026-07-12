from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        M = len(beginWord)

        adj_patterns = defaultdict(list)
        for word in wordList:
            for i in range(M):
                pattern = word[:i] + '*' + word[i+1:]
                adj_patterns[pattern].append(word)
        q = deque([(beginWord,1)])
        visited = set([beginWord])
        while q:
            current_word, steps = q.popleft()
            if current_word == endWord:
                return steps
                
            for i in range(M):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                for neighbor in adj_patterns[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor,steps + 1))
                adj_patterns[pattern] = []
        return 0

        