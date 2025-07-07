"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def insertInbetween(head):
            curr = head
            while curr:
                node = Node(curr.val)
                node.next = curr.next
                curr.next = node
                curr = curr.next.next

        def CopyRandomPointers(head):
            curr = head
            while curr:
                if curr.random:
                    curr.next.random = curr.random.next
                curr = curr.next.next

        def getDeepCopyList(head):
            temp = head
            dummy = Node(-1)
            curr = dummy
            while temp:
                curr.next = temp.next
                curr = curr.next
                temp.next = curr.next
                temp = temp.next
            return dummy.next

        insertInbetween(head)
        CopyRandomPointers(head)
        return getDeepCopyList(head)