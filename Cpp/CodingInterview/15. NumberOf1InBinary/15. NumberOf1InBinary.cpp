// 输入一个32位整数，输出该数二进制表示中1的个数。
// 注意：
// 负数在计算机中用其绝对值的补码来表示。

// 样例1
// 输入：9
// 输出：2
// 解释：9的二进制表示是1001，一共有2个1。

// 样例2
// 输入：-2
// 输出：31
// 解释：-2在计算机里会被表示成11111111111111111111111111111110，
//       一共有31个1。

class Solution {
public:
    int NumberOf1(int n) {
        // M1. 转为无符号数
        int count = 0;
        unsigned int un = n;
        while(un) count += un & 1, un >>= 1;
        return count;

        // M2. 左移1标志位
        int count = 0;
        unsigned int flag = 1;
        while (flag)
        {
            if (n & flag)
                count++;

            flag = flag << 1;
        }

        return count;

        // M3. 位运算规律
        int count = 0;

        while (n)
        {
            ++count;
            n = (n - 1) & n;
        }

        return count;

    }
};