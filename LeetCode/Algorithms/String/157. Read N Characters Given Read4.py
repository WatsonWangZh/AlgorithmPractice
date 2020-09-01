# Given a file and assume that you can only read the file using a given method read4, 
# implement a method to read n characters.
# Method read4:
# The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.
# The return value is the number of actual characters read.
# Note that read4() has its own file pointer, much like FILE *fp in C.
# Definition of read4:
#     Parameter:  char[] buf
#     Returns:    int
# Note: buf[] is destination not source, the results from read4 will be copied to buf[]
# Below is a high level example of how read4 works:
# File file("abcdefghijk"); // File is "abcdefghijk", initially file pointer (fp) points to 'a'
# char[] buf = new char[4]; // Create buffer with enough space to store characters
# read4(buf); // read4 returns 4. Now buf = "abcd", fp points to 'e'
# read4(buf); // read4 returns 4. Now buf = "efgh", fp points to 'i'
# read4(buf); // read4 returns 3. Now buf = "ijk", fp points to end of file
 
# Method read:
# By using the read4 method, implement the method read that reads n characters from the file and store it in the buffer array buf. 
# Consider that you cannot manipulate the file directly.
# The return value is the number of actual characters read.
# Definition of read:
#     Parameters:	char[] buf, int n
#     Returns:	int
# Note: buf[] is destination not source, you will need to write the results to buf[]
 
# Example 1:
# Input: file = "abc", n = 4
# Output: 3
# Explanation: After calling your read method, buf should contain "abc". 
# We read a total of 3 characters from the file, so return 3. 
# Note that "abc" is the file's content, not buf. 
# buf is the destination buffer that you will have to write the results to.

# Example 2:
# Input: file = "abcde", n = 5
# Output: 5
# Explanation: After calling your read method, buf should contain "abcde". 
# We read a total of 5 characters from the file, so return 5.

# Example 3:
# Input: file = "abcdABCD1234", n = 12
# Output: 12
# Explanation: After calling your read method, buf should contain "abcdABCD1234". 
# We read a total of 12 characters from the file, so return 12.

# Example 4:
# Input: file = "leetcode", n = 5
# Output: 5
# Explanation: After calling your read method, buf should contain "leetc". 
# We read a total of 5 characters from the file, so return 5.
 
# Note:
# Consider that you cannot manipulate the file directly, the file is only accesible for read4 but not for read.
# The read function will only be called once for each test case.
# You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.

"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        # 这道题相当于说我们每次读取文件里面的所有字符都是先由read4(buf)这个函数去读取，
        # read4每次最多读取4个字符，read4的buf里最多有4个字符
        # 然后，每次调用read4(buf)这个函数就是直接返回他这一次读取了多少个字符，
        # buf的前n个(n是他的返回值)是他这一次都读入了哪些字符，
        # 所以相当于有两个返回值，读取字符的个数n, 以及这一次读取buf里面装了哪些字符
        # 然后现在要设计一个read函数，他的buf里面一次性最多能装n个字符，然后就是这个n和文件总长度的关系
        # 但是read函数不能直接接触文件，每次的读入都要借用read4(buf)函数，
        # 所以其实read函数是利用read4函数来读取文件（字符串）
        # 也就是说read函数自己也要返回一个buf,然后用read4的buf拼接成read函数的buf,
        # 我们自己也不用声明buf,因为这个函数要自带这个buf

        tmp = [""] * 4
        idx = 0

        while True:
            cnt = read4(tmp)
            cnt = min(cnt, n-idx)
            
            for i in range(cnt):
                buf[idx] = tmp[i]
                idx += 1

            if idx == n or cnt < 4:
                return idx