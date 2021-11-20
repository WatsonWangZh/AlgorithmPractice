# Design and implement a data structure for Least Recently Used (LRU) cache. 
# It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key 
# if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. 
# When the cache reached its capacity, it should invalidate the least recently used item 
# before inserting a new item.
# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

class LRUCache(object):
    
    # 思想:首先，涉及查询，考虑用字典来存储。
    # 难点 - 如何找到哪个节点最久没被使用？
    # 定义一个双向链表，尾部的节点最久没被使用。每次访问某节点时，删除该节点，并把该节点放在头部。
    # 注意双向链表的head和tail没有数据。

    class Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next, self.prev = None, None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.dic = {}    # self.dic[key] = Node(key, value)
        self.head, self.tail = self.Node(-1,-1) , self.Node(-1,-1)
        self.head.next, self.tail.prev = self.tail, self.head

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None, None

    def insertNode(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev, self.head.next = node, node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        else:
            node = self.dic[key]
            self.removeNode(node)
            self.insertNode(node)
            return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            node = self.dic[key]
            self.removeNode(node)
            self.insertNode(node)
            node.value = value
        else:
            # Remove the tailest node
            if self.size == self.capacity:
                remove = self.tail.prev
                self.removeNode(remove)
                del self.dic[remove.key]
                self.size -= 1
            # Insert the headest node
            node = self.Node(key, value)
            self.insertNode(node)
            self.dic[key] = node
            self.size += 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)