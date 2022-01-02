"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new = Node(insertVal)
        if not head:
            new.next = new
            return new
        largest = self.findMax(head)
        if insertVal >= largest.val or insertVal <= largest.next.val:
            new.next = largest.next
            largest.next = new
            return head
        prev = head
        node = head.next
        while True:
            if prev.val <= insertVal and insertVal <= node.val:
                prev.next = new
                new.next = node
                return head
            prev = node
            node = node.next
    
    def findMax(self, head):
        largest = head
        node = head.next
        while node != head:
            if node.val >= largest.val:
                largest = node
            node = node.next
        return largest
