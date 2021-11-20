# You are given two non-empty linked lists representing two non-negative 
# integers. The digits are stored in reverse order and each of their 
# nodes contain a single digit. Add the two numbers and return it 
# as a linked list.
# You may assume the two numbers do not contain any leading zero, 
# except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

import re

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self,l1,l2):    
        if (not l1 or not l2):
            return l1 if not l2 else l2
        k1 , k2  = l1 , l2
        k1.val += k2.val
        k1.val, carry = k1.val % 10, k1.val //10
        while(k1.next and k2.next):
            k1 = k1.next
            k2 = k2.next
            k1.val += k2.val + carry
            k1.val,carry = k1.val % 10, k1.val //10
        if k2.next:
            k1.next = k2.next
        while carry != 0 and k1.next:
            k1 = k1.next
            k1.val += carry
            k1.val, carry = k1.val % 10, k1.val //10
        if carry != 0:
            k1.next = ListNode(1)
        return l1

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
        result.append(node.val)
        node = node.next
    return result

def main():
    
    expression = input()
    expression = expression.replace(' ', '')
    result = re.split('\((.*?)\)', expression)
    expression1, expression2 = result[1], result[3]
    node1, node2 = get_node_chain(expression1), get_node_chain(expression2)
    print(output_node_chain(node1))
    print(output_node_chain(node2))

    s = Solution()
    res_node = s.addTwoNumbers(node1, node2)
    print(output_node_chain(res_node))

if __name__ == '__main__': 
    main()