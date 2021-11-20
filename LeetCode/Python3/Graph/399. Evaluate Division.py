# Equations are given in the format A / B = k, where A and B are variables represented as strings, 
# and k is a real number (floating point number). 
# Given some queries, return the answers. If the answer does not exist, return -1.0.
# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].
# The input is: vector<pair<string, string>> equations, 
# vector<double>& values, vector<pair<string, string>> queries , 
# where equations.size() == values.size(), and the values are positive. 
# This represents the equations. Return vector<double>.
# According to the example above:
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
# The input is always valid. 
# You may assume that evaluating the queries will result in no division by zero 
# and there is no contradiction.
# Hints:
# Do you recognize this as a graph problem?

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # M1. 哈希建表 模拟 
        division = collections.defaultdict(list)
        for (x, y), val in zip(equations, values):
            division[x].append((y, val))
            division[y].append((x, 1/val))
        
        res = []
        for q1, q2 in queries:
            if q1 not in division or q2 not in division:
                res.append(-1.0)
                continue
                
            found = False
            q = [(q1, 1.0, set([q1]))]

            while q:
                x, total, visited = q.pop(0)
                if x == q2:
                    found = True
                    break
                for y, val in division[x]:
                    if y not in visited:
                        q.append((y, total*val, visited.union(y)))
            
            if not found:
                res.append(-1.0)
            else:
                res.append(total)
        return res 

        # M2. 并查集