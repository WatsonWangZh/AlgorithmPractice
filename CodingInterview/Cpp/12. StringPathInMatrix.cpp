// 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
// 路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
// 如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。

// 注意：
// 输入的路径不为空；
// 所有出现的字符均为大写英文字母；
// 样例
// matrix=
// [
//   ["A","B","C","E"],
//   ["S","F","C","S"],
//   ["A","D","E","E"]
// ]
// str="BCCE" , return "true" 
// str="ASAE" , return "false"

// DFS O(n^2 * 3^k)
// 在深度优先搜索中，最重要的就是考虑好搜索顺序。
// 我们先枚举单词的起点，然后依次枚举单词的每个字母。
// 过程中需要将已经使用过的字母改成一个特殊字母，以避免重复使用字符。
// 时间复杂度分析：单词起点一共有 n^2 个，
// 单词的每个字母一共有上下左右四个方向可以选择，但由于不能走回头路，所以除了单词首字母外，仅有三种选择。
// 所以总时间复杂度是 O(n^2 * 3^k)。

#include<vector>
#include<string>
using namespace std;
class Solution {
public:
    bool hasPath(vector<vector<char>>& matrix, string str) {
        for (int i = 0; i < matrix.size(); i ++ )
            for (int j = 0; j < matrix[i].size(); j ++ )
                if (dfs(matrix, str, 0, i, j))
                    return true;
        return false;
    }

    bool dfs(vector<vector<char>> &matrix, string &str, int u, int x, int y) {
        if (matrix[x][y] != str[u]) return false;
        if (u == str.size() - 1) return true;
        int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};
        char t = matrix[x][y];
        matrix[x][y] = '*';
        for (int i = 0; i < 4; i ++ ) {
            int a = x + dx[i], b = y + dy[i];
            if (a >= 0 && a < matrix.size() && b >= 0 && b < matrix[a].size()) {
                if (dfs(matrix, str, u + 1, a, b)) return true;
            }
        }
        matrix[x][y] = t;
        return false;
    }
};