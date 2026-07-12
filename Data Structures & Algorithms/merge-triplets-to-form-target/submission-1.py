class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for t in triplets:
            a,b,c = t
            if a > target[0] or b > target[1] or c > target[2]:
                triplets.remove(t)
        for pos in range(3):
            target_elem = target[pos]
            found = False
            for triplet in triplets:
                if triplet[pos] == target_elem:
                    found = True
                    break
            if not found:
                return False
        return True
        