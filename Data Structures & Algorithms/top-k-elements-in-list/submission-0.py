class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #the first thing is to loop throught the array and then count it and store it and then return 
        # the problem here is to return how many times k 
        #if i have a new int add to a dict and then 
        # use the get method to increment it by 1
        #loops throught the my-dict items values and then get the top of it
        # get the top k i mean 0 to k of the sorted list 
        if k <=0:
            return []
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num,0) + 1
        my_dict_list = list(my_dict.items())
        my_dict_list.sort(key=lambda x: x[1],reverse=True)
        answer= []
        for index,item in enumerate(my_dict_list):
            if index < k :
                answer.append(item[0])
        return answer

        