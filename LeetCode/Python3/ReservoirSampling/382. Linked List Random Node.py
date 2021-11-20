# Given a singly linked list, return a random node's value from the linked list. 
# Each node must have the same probability of being chosen.
# Follow up:
# What if the linked list is extremely large 
# and its length is unknown to you? Could you solve this efficiently without using extra space?

# Example:
# // Init a singly linked list [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
# // getRandom() should return either 1, 2, or 3 randomly. 
# Each element should have equal probability of returning.
# solution.getRandom();

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        # M1.定长链表等概率抽取一个数据
        # MM1.two pass method O(1)
        # self.head = head
        # self.length = 0
        # while head:
        #     self.length += 1
        #     head = head.next

        # MM2.tricky method 空间复杂度O(n)
        # self.lst = []
        # p = head
        # while p:
        #     self.lst.append(p.val)
        #     p = p.next

        # M2. # 从长度未知的海量数据流中随机等概率抽取一个数据
        # 蓄水池采样(Reservoir Sampling)算法
        # 算法描述
        # 1.先选取数据流中的前k个元素，保存在集合A中；
        # 2.从第j（k + 1 <= j <= n）个元素开始，每次先以概率p = k/j选择是否让第j个元素留下。
        # 若j被选中，则从A中随机选择一个元素并用该元素j替换它；否则直接淘汰该元素；
        # 3.重复步骤2直到结束，最后集合A中剩下的就是保证随机抽取的k个元素。
        # 作者：张大虎
        # 链接：https://www.jianshu.com/p/63f6cf19923d
        self.head = head

        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        # M1.定长链表等概率抽取一个数据
        # MM1.two pass method 空间复杂度O(1)
        # pointer = self.head
        # index = random.randrange(self.length)
        # for i in range(index):
        #     pointer = pointer.next
        # return pointer.val

        # MM2.tricky method 空间复杂度O(n)
        # idx = random.randrange(len(self.lst))
        # return self.lst[idx]

        # M2.蓄水池采样(Reservoir Sampling)算法
        node, n = self.head, 0
        res = 0
        while node:
            if random.randint(0, n) == 0:
                res = node.val
            node, n = node.next, n+1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()