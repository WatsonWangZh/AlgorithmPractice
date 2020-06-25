# Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. 
# The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 10^4. 
# Reconstruction means building a shortest common supersequence of the sequences in seqs 
# (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). 
# Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

# Example 1:
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3]]
# Output:
# false
# Explanation:
# [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

# Example 2:
# Input:
# org: [1,2,3], seqs: [[1,2]]
# Output:
# false
# Explanation:
# The reconstructed sequence can only be [1,2].

# Example 3:
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
# Output:
# true
# Explanation:
# The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

# Example 4:
# Input:
# org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
# Output:
# true

# UPDATE (2017/1/8):
# The seqs parameter had been changed to a list of list of strings (instead of a 2d array of strings). 
# Please reload the code definition to get the latest changes.

class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        # https://blog.csdn.net/liuchenjane/article/details/52983666
        # 先判断seqs里的每一个seq是否是org里的子序列，
        # 首先记载每个元素在org中的下标，如果子序列的元素中，后面元素的下标比前面的小，则不是子序列。
        # 然后，对于判断由这些子序列是否可以重构原始的org。
        # 后面的seqs中必须满足以下下条件，对于org中任意相邻的两个数x和y，在seqs中必定存在相邻的x和y来表示它们的相对次序。
        # 否则，x和y的位置是可交换的，与题目中的唯一重构的要求相悖。
        
        if not seqs or not org:
            return False

        idx = {}
        for i, c in enumerate(org):
            idx[c] = i

        # org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
        pair = {}
        for seq in seqs:
            for i in range(len(seq)):
                # 子序列中有org中未出现的字母
                if seq[i] not in idx:
                    return False
                # 子序列中相邻的字符顺序与org中不一致
                if i > 0 and idx[seq[i-1]] >= idx[seq[i]]:
                    return False
                # 子序列中相邻的字符顺序与org中一致
                if i > 0 and idx[seq[i-1]]+1 == idx[seq[i]]: 
                    pair[idx[s[i-1]]] = 1
            if seq and seq[-1] == org[-1]:
                pair[len(org)-1] = 1        
                    
        for i in range(len(org)):
            # org中前后相邻的字母没有完全出现在子序列中
            if i not in pair:
                return False
        return True 