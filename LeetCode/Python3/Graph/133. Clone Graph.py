# Given a reference of a node in a connected undirected graph,
#  return a deep copy (clone) of the graph.
#  Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

# Example:
# Input:
# {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
# Explanation:
# Node 1's value is 1, and it has two neighbors: Node 2 and 4.
# Node 2's value is 2, and it has two neighbors: Node 1 and 3.
# Node 3's value is 3, and it has two neighbors: Node 2 and 4.
# Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 
# Note:
# The number of nodes will be between 1 and 100.
# The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
# Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
# You must return the copy of the given node as a reference to the cloned graph.

# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # 因为图中可能存在环，所以直接将节点和它的相邻节点进行复制，
        # 并对它的相邻节点进行相同操作可能会进入死循环。
        # 为了避免循环访问，要对已经复制过的节点进行缓存，
        # 我们通过一个由标志和节点组成的字典来记录已经访问过的节点。
        # 当我们通过相邻关系来访问一个节点时，如果它是第一次被访问，
        # 则要将其加入一个栈中，在栈中的元素表示要继续访问它相邻的元素，
        # 并记录它已经被访问过，同时要跟新已经被访问过的节点中与其相邻的节点的邻居列表。
        # 当栈为空时，表示所有的节点都已经访问完毕，图也复制成功。
        d = {}
        stack = [node]
        visited = set()
        while stack:
            u = stack.pop()
            if u not in d:
                d[u] = Node(u.val, [])
            if u in visited:
                continue
            visited.add(u)
            for neighbor in u.neighbors:
                if neighbor not in d:
                    d[neighbor] = Node(neighbor.val, [])
                d[u].neighbors.append(d[neighbor])
                stack.append(neighbor)
        return d[node]
