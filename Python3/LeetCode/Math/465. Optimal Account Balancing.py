# A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. 
# Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. 
# Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), 
# the transactions can be represented as [[0, 1, 10], [2, 0, 5]].
# Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.

# Note:
# A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
# Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.

# Example 1:
# Input:
# [[0,1,10], [2,0,5]]
# Output:
# 2
# Explanation:
# Person #0 gave person #1 $10.
# Person #2 gave person #0 $5.
# Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

# Example 2:
# Input:
# [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
# Output:
# 1
# Explanation:
# Person #0 gave person #1 $10.
# Person #1 gave person #0 $1.
# Person #1 gave person #2 $5.
# Person #2 gave person #0 $5.
# Therefore, person #1 only need to give person #0 $4, and all debt is settled.

import collections
import itertools
class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        balances = collections.defaultdict(int)
        people = set()
        for giver, receiver, amount in transactions:
            balances[giver] -= amount
            balances[receiver] += amount
            # 求并集
            people |= {giver, receiver}
            
        for person_id, balance in balances.items():
            if balance == 0:
                people.discard(person_id)
                balances.pop(person_id)
        
        people_list = list(people)
        
        def dfs(people_list):
            if not people_list:
                return 0
            people = set(people_list)
            for i in range(2, len(people_list) + 1):
                for persons in itertools.combinations(people_list, i):
                    if sum(balances[p] for p in persons) == 0:
                        people -= set(persons)
                        return dfs(list(people)) + len(persons) - 1
        
        return dfs(people_list)