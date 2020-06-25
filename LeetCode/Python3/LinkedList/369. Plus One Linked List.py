# Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list.

# Example :
# Input: [1,2,3]
# Output: [1,2,4]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # https://www.cnblogs.com/grandyang/p/5626389.html
        # M1. 两次翻转
        # 这道题给了我们一个链表，用来模拟一个三位数，表头是高位，现在让我们进行加1运算，
        # 这道题的难点在于链表无法通过坐标来访问元素，只能通过遍历的方式进行，
        # 而这题刚好让我们从链尾开始操作，从后往前，遇到进位也要正确的处理，
        # 最后还有可能要在开头补上一位。那么我们反过来想，如果链尾是高位，那么进行加1运算就方便多了，
        # 直接就可以边遍历边进行运算处理，那么我们可以做的就是先把链表翻转一下，
        # 然后现在就是链尾是高位了，我们进行加1处理运算结束后，再把链表翻转回来即可。

    #     head = self.reverse(head)
    #     dummy = ListNode(0)
    #     dummy.next = head

    #     cur = head
    #     carry = 1

    #     while carry > 0 or cur:
    #         cur.val += carry
    #         carry = cur.val / 10
    #         cur.val %= 10

    #         if carry and cur.next is None:
    #             cur.next = ListNode(0)

    #         cur = cur.next

    #     return self.reverse(dummy.next)
        
    # def reverse(self, head):
    #     prev = None
    #     while head:
    #         temp = head.next
    #         head.next = prev
    #         prev = head
    #         head = temp
    #     return prev

        # M2. Trick 
        # 下面这种方法比较巧妙了，思路是遍历链表，找到右起第一个不为9的数字，
        # 如果找不到这样的数字，说明所有数字均为9，那么在表头新建一个值为0的新节点，进行加1处理，
        # 然后把右边所有的数字都置为0即可。举例来说：
        # 比如1->2->3，那么第一个不为9的数字为3，对3进行加1，变成4，右边没有节点了，所以不做处理，返回1->2->4。
        # 再比如说8->9->9，找第一个不为9的数字为8，进行加1处理变成了9，然后把后面的数字都置0，得到结果9->0->0。
        # 再来看9->9->9的情况，找不到不为9的数字，那么再前面新建一个值为0的节点，进行加1处理变成了1，
        # 把后面的数字都置0，得到1->0->0->0。

        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        i = dummy
        j = dummy
        while j.next:
            j = j.next
            if j.val != 9:
                i = j

        i.val += 1
        i = i.next

        while i:
            i.val = 0
            i = i.next

        if dummy.val == 0:
            return dummy.next
        return dummy
