# Given a positive 32-bit integer n, 
# you need to find the smallest 32-bit integer which has exactly the same digits 
# existing in the integer n and is greater in value than n. 
# If no such positive 32-bit integer exists, you need to return -1.

# Example 1:
# Input: 12
# Output: 21
 
# Example 2:
# Input: 21
# Output: -1

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 这道题给了我们一个数字，让我们对各个位数重新排序，求出刚好比给定数字大的一种排序，如果不存在就返回-1。
        # 这道题给的例子的数字都比较简单，我们来看一个复杂的，比如12443322，这个数字的重排序结果应该为13222344，
        # 如果我们仔细观察的话会发现数字变大的原因是左数第二位的2变成了3，细心的童鞋会更进一步的发现后面的数字由降序变为了升序，
        # 这也不难理解，因为我们要求刚好比给定数字大的排序方式。那么我们再观察下原数字，看看2是怎么确定的，
        # 我们发现，如果从后往前看的话，2是第一个小于其右边位数的数字，因为如果是个纯降序排列的数字，做任何改变都不会使数字变大，
        # 直接返回-1。知道了找出转折点的方法，再来看如何确定2和谁交换，这里2并没有跟4换位，而是跟3换了，那么如何确定的3？
        # 其实也是从后往前遍历，找到第一个大于2的数字交换，然后把转折点之后的数字按升序排列就是最终的结果了。
        # 最后记得为防止越界要转为长整数型，然后根据结果判断是否要返回-1即可。
        # 过程图解: https://blog.csdn.net/fuxuemingzhu/article/details/82113731
        
        # Edge Case
        str_n = list(str(n))
        if len(str_n) == 1:
            return -1
        
        # Finding first decreasing element
        curr = len(str_n) - 1
        while curr > 0:
            if int(str_n[curr-1]) >= int(str_n[curr]):
                curr -= 1
            else:
                break
        if curr == 0:
            return -1
        
        # Finding number just larger than the above decreasing element
        temp_index = curr 
        while temp_index < len(str_n) and int(str_n[temp_index]) > int(str_n[curr - 1]):
            temp_index += 1
            
        # Switching it with the above decreasing element
        self.switch(str_n, curr - 1, temp_index - 1)
        
        # Reversing the append elements
        self.reverse(str_n, curr, len(str_n) - 1)
        
        # Producing the result
        result = int(''.join(str_n))
        if result > 2147483648:
            return -1
        
        return result
    
        
    def reverse(self, n, start, end):
        while start < end:
            self.switch(n, start, end)
            start += 1
            end -= 1
            
    def switch(self, n, idx1, idx2):
        temp = n[idx1]
        n[idx1] = n[idx2]
        n[idx2] = temp
