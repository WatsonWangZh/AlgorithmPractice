// 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
// 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

// 样例
// 输入数组：
// [
//   [1,2,8,9]，
//   [2,4,9,12]，
//   [4,7,10,13]，
//   [6,8,11,15]
// ]
// 如果输入查找数值为7，则返回true，
// 如果输入查找数值为5，则返回false。

// (单调性扫描) O(m+n)
// 核心在于发现每个子矩阵右上角的数的性质：
// 如下图所示，x左边的数都小于等于x，x下边的数都大于等于x。
// 从整个矩阵的右上角开始枚举，假设当前枚举的数是 x：
// 如果 x 等于target，则说明我们找到了目标值，返回true；
// 如果 x 小于target，则 x 左边的数一定都小于target，我们可以直接排除当前一整行的数；
// 如果 x 大于target，则 x 下边的数一定都大于target，我们可以直接排序当前一整列的数；
// 排除一整行就是让枚举的点的横坐标加一，排除一整列就是让纵坐标减一。
// 当我们排除完整个矩阵后仍没有找到目标值时，就说明目标值不存在，返回false。
// 时间复杂度分析
// 每一步会排除一行或者一列，矩阵一共有 m 行，n 列，所以最多会进行 m+n 步。
// 所以时间复杂度是 O(m+n)。

#include<vector>
using namespace std;
class Solution {
public:
    bool searchArray(vector<vector<int>> array, int target) {
        if (array.empty() || array[0].empty()) return false;
        int i = 0, j = array[0].size() - 1;
        while (i < array.size() && j >= 0) {
            if (array[i][j] == target) 
                return true;
            if (array[i][j] > target) 
                j -- ;
            else 
                i ++ ;
        }
        return false;
    }
};