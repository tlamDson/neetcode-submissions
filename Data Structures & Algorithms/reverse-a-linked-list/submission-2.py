# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            next_node = curr.next # lưu lại đường lui
            curr.next = prev # trỏ nexst về kia
            prev = curr # dich con trỏ prev lên
            curr = next_node # dịch con trỏ curr lên
        return prev
        