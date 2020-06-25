# Given a singly linked list, group all odd nodes together followed by the even nodes. 
# Please note here we are talking about the node number and not the value in the nodes.
# You should try to do it in place. 
# The program should run in O(1) space complexity and O(nodes) time complexity.

# Example 1:
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL

# Example 2:
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL

# Note:
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        # M1. 就地拆分
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = head.next
        p = head.next.next 
        
        while p:
            odd.next = p
            odd = p
            p = p.next
            if p:
                even.next = p
                even = p
                p = p.next
        odd.next = even_head
        even.next = None
        return head

        # M2. dummy Node
        # we'll be defining a dummy node for each 
        # of the odd and the even lists
        odds = ListNode('odd')
        evens = ListNode('even')
        
        oddsHead, evensHead = None, None
        # oddsHead will become the head of the new list
        oddsHead = odds
        # evensHead will be joined to the end of odd list
        evensHead = evens
        # first element is odd
        isOdd = True

        
        # traverse the list and keep on appending
        while head :
            if isOdd:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next
            isOdd = not isOdd
            head = head.next
        
        evens.next = None
        odds.next = evensHead.next # because evensHead had first node as dummy
        return oddsHead.next