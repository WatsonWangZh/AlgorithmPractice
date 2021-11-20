# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.

# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# Definition for singly-linked list.
import re

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None: return l2
        elif l2 is None: return l1
        
        use_l1 = l1.val <= l2.val
        if use_l1:
            itr1 = l1
            itr2 = l2
        else:
            itr1 = l2
            itr2 = l1
        
        while itr1.next is not None and itr2 is not None:
            if itr1.next.val >= itr2.val:
                tmp1 = itr1.next
                itr1.next = itr2
                tmp2 = itr2.next
                itr2.next = tmp1
                itr2 = tmp2
                itr1 = itr1.next
            else:
                itr1 = itr1.next
                
        while itr2 is not None:
            itr1.next = itr2
            itr1 = itr2
            itr2 = itr2.next
            
        if use_l1: return l1
        else: return l2

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
    expression = "1->2->4, 1->3->4"
    expression = expression.replace(' ', '')
    result = re.split(',', expression)
    node1, node2 = get_node_chain(result[0]), get_node_chain(result[1])
    res_list = s.mergeTwoLists(node1, node2)
    print("->".join(output_node_chain(res_list)))

if __name__ == "__main__":
    main()