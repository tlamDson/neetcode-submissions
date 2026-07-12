# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k:
            return head
        # đảo ngược k node đầu tiên
        # head trở thành trở thành tail của cái đảo ngược
        # prev trở thành head
        prev, curr_node = None, head
        for _ in range(k):
            next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node
        # 
        head.next = self.reverseKGroup(curr_node, k)
        return prev
        

        