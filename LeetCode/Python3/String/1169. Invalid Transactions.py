# A transaction is possibly invalid if:
# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
# Each transaction string transactions[i] consists of comma separated values 
# representing the name, time (in minutes), amount, and city of the transaction.
# Given a list of transactions, return a list of transactions that are possibly invalid.  
# You may return the answer in any order.

# Example 1:
# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, 
# have the same name and is in a different city. Similarly the second one is invalid too.

# Example 2:
# Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# Output: ["alice,50,1200,mtv"]

# Example 3:
# Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# Output: ["bob,50,1200,mtv"]

# Constraints:
# transactions.length <= 1000
# Each transactions[i] takes the form "{name},{time},{amount},{city}"
# Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
# Each {time} consist of digits, and represent an integer between 0 and 1000.
# Each {amount} consist of digits, and represent an integer between 0 and 2000.

# Hints:
# Split each string into four arrays.
# For each transaction check if it's invalid, 
# you can do this with just a loop with help of the four arrays generated on step 1.
# At the end you perform O(N ^ 2) operations.

import collections
class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        # M1. 模拟 蛮力算法 O(n^2)
        res=[]
        for i in range(len(transactions)):
            transactions[i]=transactions[i].split(',')
        for i in range(len(transactions)):
            if int(transactions[i][2])>1000:
                res.append(str(','.join(transactions[i])))
            for j in range(i+1,len(transactions)):       
                if abs(int(transactions[i][1])-int(transactions[j][1]))<=60 and transactions[i][3]!=transactions[j][3] \
                    and transactions[i][0]==transactions[j][0]:
                    res.append(str(','.join(transactions[i])))
                    res.append(str(','.join(transactions[j])))
        return list(set(res))

        # M2. 分组排序过滤 O(nlgn)
        AMOUNT, MINUTES = 1000, 60
        trans = map(lambda x: (x[0], int(x[1]), int(x[2]), x[3]),
                    (transaction.split(',') for transaction in transactions))
        # 按时间排序
        trans.sort(key=lambda t: t[1])
        # 按姓名分组
        trans_indexes = collections.defaultdict(list)
        for i, t in enumerate(trans):
            trans_indexes[t[0]].append(i)
            
        res = []
        # 核查每人的交易是否合法
        for name, indexes in trans_indexes.iteritems():
            left, right = 0, 0
            for i, t_index in enumerate(indexes):
                t = trans[t_index]
                # 金额非法
                if (t[2] > AMOUNT):
                    res.append("{},{},{},{}".format(*t))
                    continue
                # 找出交易时间差小于60min的交易区间，由于已经按时间排序，故left和right可以确定上下界
                while left+1 < len(indexes) and trans[indexes[left]][1] < t[1]-MINUTES:
                    left += 1
                while right+1 < len(indexes) and trans[indexes[right+1]][1] <= t[1]+MINUTES:
                    right += 1
                # 在小于60min内找city不一样的交易
                for i in range(left, right+1):
                    if trans[indexes[i]][3] != t[3]:
                        res.append("{},{},{},{}".format(*t))
                        break
        return res
