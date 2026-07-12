class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = []
        for char in s:
            if char.isdigit():
                curr_num = curr_num*10 + int(char)
            elif char == '[':
                stack.append((curr_str,curr_num))
                curr_num = 0
                curr_str = []
            elif char == ']':
                last_str, num = stack.pop()
                curr_str = last_str + (curr_str*num)
            else:
                curr_str.append(char)
        return "".join(curr_str)
        