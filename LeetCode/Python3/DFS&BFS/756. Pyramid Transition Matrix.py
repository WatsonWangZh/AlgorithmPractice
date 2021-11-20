# We are stacking blocks to form a pyramid. Each block has a color which is a one letter string.
# We are allowed to place any color block C on top of two adjacent blocks of colors A and B, if and only if ABC is an allowed triple.
# We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. 
# Each allowed triple is represented as a string of length 3.
# Return true if we can build the pyramid all the way to the top, otherwise false.

# Example 1:
# Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
# Output: true
# Explanation:
# We can stack the pyramid like this:
#     A
#    / \
#   G   E
#  / \ / \
# B   C   D
# We are allowed to place G on top of B and C because BCG is an allowed triple.  
# Similarly, we can place E on top of C and D, then A on top of G and E.
 
# Example 2:
# Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
# Output: false
# Explanation:
# We can't stack the pyramid to the top.
# Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
 
# Note:
# bottom will be a string with length in range [2, 8].
# allowed will have length in range [0, 200].
# Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.

# 全组合求所有可能结果采用BFS，而不是DFS。
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        # 在当前bottom的基础上，递推上一层的结点，直到结点只包含1个 → 构造完成。
        # 1）递推上一层：建一个 dic 拆分三元组，例如(X,Y,Z)，则记录dic[(X,Y)] = [z]；
        # 2）allLists 存储上一层可能包含的结点。例如[[‘X’,’Y’], [‘Z’]]，表示上一层可能为’XZ’或’YZ’；
        # 3）helper函数用来组合，在 allLists 基础上构造上一层可能的状态。例如[[‘X’,’Y’], [‘Z’]] → [‘XZ’, ‘YZ’]，（其中combs = [‘XZ’, ‘YZ’]表示上一层可能的状态）；
        # 4）省时间，cache 存储已判断过的bottom，记录以该bottom为底，是否可构造金字塔。
        # 例如在递归过程中，’XZZ’可以构造金字塔，则 cache[‘XZZ’] = True，下次再遇到’XZZ’就无需判断了

        self.dic = {}
        self.cache = {}
        allowed = set(allowed)
        for allow in allowed:
            if allow[:2] not in self.dic:
                self.dic[allow[:2]] = [allow[-1]]
            else:
                self.dic[allow[:2]].append(allow[-1])
        return self.dfs(bottom)

    def dfs(self, bottom):
        if len(bottom) == 2:
            return bottom in self.dic

        if bottom in self.cache:
            return self.cache[bottom]

        allLists = []
        for i in range(len(bottom)-1):
            if bottom[i:i+2] not in self.dic:
                self.cache[bottom] = False
                return False
            allLists.append(self.dic[bottom[i:i+2]])

        # BFS 得到所有可能组合
        combs = self.helper(allLists)

        # DFS验证每组可能组合
        for comb in combs:
            if self.dfs(comb):
                self.cache[comb] = True
                return True

        self.cache[bottom] = False
        return False  

    def helper(self, allLists):
        queue = ['']
        for List in allLists:
            for _ in range(len(queue)):
                node = queue.pop(0)
                for c in List:
                    queue.append(node + c)
        return queue


# 全组合采用的DFS，TLE
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        # 在当前bottom的基础上，递推上一层的结点，直到结点只包含1个 → 构造完成。
        # 1）递推上一层：建一个 dic 拆分三元组，例如(X,Y,Z)，则记录dic[(X,Y)] = [z]；
        # 2）allLists 存储上一层可能包含的结点。例如[[‘X’,’Y’], [‘Z’]]，表示上一层可能为’XZ’或’YZ’；
        # 3）helper函数用来组合，在 allLists 基础上构造上一层可能的状态。例如[[‘X’,’Y’], [‘Z’]] → [‘XZ’, ‘YZ’]，（其中combs = [‘XZ’, ‘YZ’]表示上一层可能的状态）；
        # 4）省时间，cache 存储已判断过的bottom，记录以该bottom为底，是否可构造金字塔。
        # 例如在递归过程中，’XZZ’可以构造金字塔，则 cache[‘XZZ’] = True，下次再遇到’XZZ’就无需判断

        self.dic = {}
        self.cache = {}
        for allow in allowed:
            if allow[:2] not in self.dic:
                self.dic[allow[:2]] = [allow[2]]
            else:
                self.dic[allow[:2]] += [allow[2]]

        return self.dfs(bottom)

    def dfs(self, bottom):
        if len(bottom) == 1:
            return True
        if bottom in self.cache:
            return self.cache[bottom]

        allLists = []
        for i in range(len(bottom)-1):
            if bottom[i:i+2] not in self.dic:
                self.cache[bottom] = False
                return False
            allLists.append(self.dic[bottom[i:i+2]])

        combs = []
        self.helper(allLists, '', combs)

        for comb in combs:
            if self.dfs(comb):
                self.cache[comb] = True
                return True

        self.cache[bottom] = False
        return False  

    def helper(self, allLists, temp, combs):
        if not allLists:
            combs.append(temp)
            return
        for List in allLists:
            for c in List:
                self.helper(allLists[1:], temp + c, combs)
