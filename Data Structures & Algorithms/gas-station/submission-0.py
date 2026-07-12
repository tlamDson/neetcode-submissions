class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Nếu mà gas hiện tại bé hơn cost -> continue luôn
        # thử các cách còn lại 
        # nếu gặp đến idx cuối và visted chưa hết 
        # idx = 0
        if sum(gas) < sum(cost): return -1
        start = 0
        total_tank = 0
        current_tank = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            current_tank += diff
            if current_tank < 0:
                start = i + 1
                current_tank  = 0
        return start if total_tank >= 0 else -1





        
                
                
        
