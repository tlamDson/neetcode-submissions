class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        my_dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        def backtrack(start_index, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            len_word_curr_digits = my_dict[digits[start_index:start_index+ 1]]
            for j in range(len(len_word_curr_digits)):
                path.append(len_word_curr_digits[j])
                backtrack(start_index + 1, path)
                path.pop()
        backtrack(0,[])
        return res 
        
        