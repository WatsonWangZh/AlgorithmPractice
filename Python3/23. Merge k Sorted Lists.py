# Merge k sorted linked lists 
# and return it as one sorted list. 
# Analyze and describe its complexity.

# Example:
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Merge two by two solution.
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        if not lists:
            return None
        left, right = 0, len(lists) - 1;
        while right > 0:
            if left >= right:
                left = 0
            else:
                lists[left] = mergeTwoLists(lists[left], lists[right])
                left += 1
                right -= 1
        return lists[0]

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
    input_lists = ["1->4->5", "1->3->4", "2->6"]
    for i in range(len(input_lists)):
        input_lists[i] = get_node_chain(input_lists[i])
    res_lists = s.mergeKLists(input_lists)
    print("->".join(output_node_chain(res_lists)))

if __name__ == "__main__":
    main()