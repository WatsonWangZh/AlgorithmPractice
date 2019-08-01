# A linked list is given such that each node contains an additional 
# random pointer which could point to any node in the list or null.
# Return a deep copy of the list.

# Example 1:
# Input:
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer points to itself.

# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # M1.HashMap Solution
        if not head:
            return None
        
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val, None, None)
            cur = cur.next
            
        cur = head
        while cur != None:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
            
        return dic[head]
