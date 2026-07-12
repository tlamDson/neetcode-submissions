class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Initialization
        newStr = "".join(char.lower() for char in s if char.isalnum())
        if not newStr: 
            return True
        print(newStr)
        left, right = 0, len(newStr) - 1

        while left < right:
            if newStr[left] != newStr[right]:
                return False
            left +=1 
            right -= 1
        return True
        
