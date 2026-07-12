class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = self.countString(s)
        dictT = self.countString(t)
        return dictS == dictT
    
    def countString(self, s : str) -> dict[str,int]:
        dict = {}
        for index, key in enumerate(s):
            dict[key] = dict.get(key,0) + 1
        return dict

     