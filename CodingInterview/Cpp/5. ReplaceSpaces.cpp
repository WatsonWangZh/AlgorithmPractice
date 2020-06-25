// 请实现一个函数，把字符串中的每个空格替换成"%20"。
// 你可以假定输入字符串的长度最大是1000。
// 注意输出字符串的长度可能大于1000。

// 样例
// 输入："We are happy."
// 输出："We%20are%20happy."

#include<string>
using namespace std;

// M1. 线性扫描 分配新空间 O(n) O(n)
// 这个题在C++里比较好做，我们可以从前往后枚举原字符串：
// 如果遇到空格，则在string类型的答案中添加 "%20"；
// 如果遇到其他字符，则直接将它添加在答案中；

class Solution {
public:
    string replaceSpaces(string &str) {
        string res;
        for (auto x : str)
            cout << x << endl;
            if (x == ' ')
                res += "%20";
            else
                res += x;
        return res;
    }
};

// M2. 双指针末端替换 不分配新空间 O(n) O(1)
// 首先遍历一遍原数组，求出最终答案的长度length；
// 将原数组resize成length大小；
// 使用两个指针，指针i指向原字符串的末尾，指针j指向length的位置；
// 两个指针分别从后往前遍历，如果str[i] == ' '，则指针j的位置上依次填充'0', '2', '%'，这样倒着看就是"%20"；如果str[i] != ' '，则指针j的位置上填充该字符即可。
// 由于i之前的字符串，在变换之后，长度一定不小于原字符串，所以遍历过程中一定有i <= j，这样可以保证str[j]不会覆盖还未遍历过的str[i]，从而答案是正确的。
// 时间复杂度分析
// 原字符串只会被遍历常数次，所以总时间复杂度是 O(n)。

class Solution {
public:
    string replaceSpaces(string &str) {

        int len = 0;
        for (auto c : str)
            if (c == ' ')
                len += 3;
            else
                len ++ ;

        int i = str.size() - 1, j = len - 1;

        str.resize(len);

        while (i >= 0)
        {
            if (str[i] == ' ')
            {
                str[j -- ] = '0';
                str[j -- ] = '2';
                str[j -- ] = '%';
            }
            else str[j -- ] = str[i];
            i -- ;
        }
        return str;
    }
};
