class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        my_dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        def backtrack(start_index, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            letters = my_dict[digits[start_index]]
            for char in letters: 
                path.append(char)
                backtrack(start_index + 1,path)
                path.pop()
        backtrack(0,[])
        return res 
        
        