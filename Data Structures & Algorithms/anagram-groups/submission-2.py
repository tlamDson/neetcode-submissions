from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # counter thi luu index 
        # { count = {a:1,c:1,t:1},1}
        # o is maybe 0n *m where n is the lengh of str and m is the lenght of the longest string
        # the m is m where m is the number of string
        # chính counter là một dictionary 
        # thêm keys thêm value như nào 
        # 
        my_dict = {}
        res = []
        for index, string in enumerate(strs):
            counter = Counter(string)
            counter_key = tuple(sorted(counter.items()))
            if counter_key in my_dict:
                my_dict[counter_key].append(index)
            else:
                my_dict[counter_key] = [index]
        for key, value in sorted(my_dict.items()):
            l = []
            for v in value:
                l.append(strs[v])
            res.append(l)
        return res
                
            
        