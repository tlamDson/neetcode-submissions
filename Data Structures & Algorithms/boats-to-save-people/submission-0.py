class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        l, r = 0,len(people)-1
        num_boat = 0
        while l <= r:
            if people[l] + people[r] > limit:
                r-=1
                num_boat += 1
            else:
                r -=1
                l += 1
                num_boat +=1
        return num_boat
            
        