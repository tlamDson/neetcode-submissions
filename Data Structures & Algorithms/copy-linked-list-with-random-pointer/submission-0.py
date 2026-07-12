"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        node = dummy
        copyList = {}
        curr = head
        while curr:
            copyList[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            # take the current copy of the curr node
            copy = copyList[curr]
            # the copy of curr.next is the copyList[curr.next]
            copy.next = copyList.get(curr.next)
            # the copy of curr.random is copyList[curr.random]
            copy.random = copyList.get(curr.random)
            node.next = copy
            node = node.next
            curr = curr.next
        return dummy.next
            

            
        