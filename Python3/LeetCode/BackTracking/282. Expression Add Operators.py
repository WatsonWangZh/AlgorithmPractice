# Given a string that contains only digits 0-9 and a target value, 
# return all possibilities to add binary operators (not unary) +, -, or * 
# between the digits so they evaluate to the target value.

# Example 1:
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"] 

# Example 2:
# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]

# Example 3:
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]

# Example 4:
# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]

# Example 5:
# Input: num = "3456237490", target = 9191
# Output: []

class Solution(object):
    # M1.官方题解
    # def addOperators(self, num, target):
    #     """
    #     :type num: str
    #     :type target: int
    #     :rtype: List[str]
    #     """
    #     N = len(num)
    #     answers = []
    #     def recurse(index, prev_operand, current_operand, value, string):

    #         # Done processing all the digits in num
    #         if index == N:

    #             # If the final value == target expected AND
    #             # no operand is left unprocessed
    #             if value == target and current_operand == 0:
    #                 answers.append("".join(string[1:]))
    #             return
    #         # Extending the current operand by one digit
    #         current_operand = current_operand*10 + int(num[index])
    #         str_op = str(current_operand)

    #         # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
    #         # valid operand. Hence this check
    #         if current_operand > 0:

    #             # NO OP recursion
    #             recurse(index + 1, prev_operand, current_operand, value, string)
                
    #             # ADDITION
    #         string.append('+'); string.append(str_op)
    #         recurse(index + 1, current_operand, 0, value + current_operand, string)
    #         string.pop();string.pop()

    #         # Can subtract or multiply only if there are some previous operands
    #         if string:

    #             # SUBTRACTION
    #             string.append('-'); string.append(str_op)
    #             recurse(index + 1, -current_operand, 0, value - current_operand, string)
    #             string.pop();string.pop()

    #             # MULTIPLICATION
    #             string.append('*'); string.append(str_op)
    #             recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
    #             string.pop();string.pop()
    #     recurse(0, 0, 0, 0, [])    
    #     return answers

    # M2.DFS+表达式求值 O(n4^n)
    # 枚举方案时需要注意：数字不能以"0"开头，即不能出现1+01；也就是需要去掉前导零。
    # 时间复杂度分析：每个数字之间可以填+，-，*或者不填，一共四种选择，所以一共有 4n−1 种方案，
    # 每个表达式求值需要 O(n)O(n) 的时间复杂度，所以总时间复杂度是 O(n4^n)。
    
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.ans = []
        self.num = num
        self.target = target
        self.helper(0, [], 0, 0)
        return self.ans

    def helper(self, result, header, ind, multed):
        if len(self.num) == ind and self.target == result:
            self.ans.append("".join(header))
            return
        for i in range(ind, len(self.num)):
            if i > ind and int(self.num[ind]) == 0:
                return
            item = int(self.num[ind:i + 1])
            if len(header) == 0:
                header.append(str(item))
                self.helper(item, header, i + 1, item)  # 如果是第一个数字
                header.pop()
            else:
                # +
                header.append('+')
                header.append(str(item))
                self.helper(result + item, header, i + 1, item)
                header.pop()
                header.pop()
                # -
                header.append('-')
                header.append(str(item))
                self.helper(result - item, header, i + 1, -item)
                header.pop()
                header.pop()
                # *
                header.append("*")
                header.append(str(item))
                newResult = result - multed + multed * item
                self.helper(newResult, header, i + 1, multed * item)
                header.pop()
                header.pop()
        return
