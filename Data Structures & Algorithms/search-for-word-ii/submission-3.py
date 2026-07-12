class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row, col = len(board), len(board[0])
        res = []

        # Use a Trie to optimize searching multiple words at once
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = word

        def dfs(r, c, node):
            char = board[r][c]
            if char in node:
                curr_node = node[char]
            else:
                return
            # curr_node = node.get(char)
            # if not curr_node:
            #     return
            
            if '#' in curr_node:
                res.append(curr_node.pop('#'))
            
            board[r][c] = '*'
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    dfs(nr, nc, curr_node)
            board[r][c] = char
            
            # Optimization: remove empty leaf nodes
            if not curr_node:
                node.pop(char)

        for r in range(row):
            for c in range(col):
                dfs(r, c, trie)
        return res