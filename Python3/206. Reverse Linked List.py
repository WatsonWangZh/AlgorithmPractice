# Reverse a singly linked list.

# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# Follow up:
# A linked list can be reversed either iteratively or recursively.
# Could you implement both?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #wrong answer
        # p = head
        # while p:
        #     q = p.next
        #     p.next = q.next
        #     head.next = q
        #     q.next = p
        # p.next = head
        # head = head.next
        # p.next.next = None
        # return head
        
        lastNode = None
        while head:
            nextNode = head.next
            head.next = lastNode
            lastNode = head
            head = nextNode
        
        return lastNode.next

def get_node_chain(expression):
    expression_numbers = expression.split('->')
    last_node, first_node = None, None
    for expression_number in expression_numbers:
        node = ListNode(str(expression_number))
        if not last_node:
            first_node = node
        if last_node:
            last_node.next = node
        last_node = node
    return first_node

def output_node_chain(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def main():
    s = Solution()
    input_list = "5->4->3->2->1->NULL"
    res_input = s.reverseList(get_node_chain(input_list))
    print("->".join(output_node_chain(res_input)))

if __name__ == "__main__":
    main()