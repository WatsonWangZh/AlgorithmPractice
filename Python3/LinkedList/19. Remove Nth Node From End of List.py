# Given a linked list, remove the n-th node from the end of list and return its head.
# Example:

# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Note:
# Given n will always be valid.
# Follow up:
# Could you do this in one pass?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        for i in range(n):  #high_light?
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

def get_node_chain(expression):
    expression_numbers = expression.split('->')
    last_node, first_node = None, None
    for expression_number in expression_numbers:
        node = ListNode(int(expression_number))
        if not last_node:
            first_node = node
        if last_node:
            last_node.next = node
        last_node = node
    return first_node

def output_node_chain(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    return result

def main():
    s = Solution()
    list_input = get_node_chain("1->2->3->4->5")
    res_list = s.removeNthFromEnd(list_input,2)
    print("->".join(output_node_chain(res_list)))

if __name__ == "__main__":
    main()