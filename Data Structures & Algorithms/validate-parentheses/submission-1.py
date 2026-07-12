class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        mapping = {
            ')':'(',
            '}':'{',
            ']':'['}
        #loop through each character in s
        for c in s: 
            # if the character is a closing racketes
            if c in mapping:
                #check if the last character in stack is equal to mapping[c] so mapping c is basically the character
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
