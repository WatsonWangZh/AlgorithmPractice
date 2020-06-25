// 地上有一个 m 行和 n 列的方格，横纵坐标范围分别是 0∼m−1 和 0∼n−1。
// 一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格。
// 但是不能进入行坐标和列坐标的数位之和大于 k 的格子。
// 请问该机器人能够达到多少个格子？

// 样例1
// 输入：k=7, m=4, n=5
// 输出：20

// 样例2
// 输入：k=18, m=40, n=40
// 输出：1484
// 解释：当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
//       但是，它不能进入方格（35,38），因为3+5+3+8 = 19。

// 注意:
// 0<=m<=50
// 0<=n<=50
// 0<=k<=100

// BFS O(nm)
// 这是一个典型的宽度优先搜索问题，我们从 (0, 0) 点开始，
// 每次朝上下左右四个方向扩展新的节点即可。
// 扩展时需要注意新的节点需要满足如下条件：
// 之前没有遍历过，这个可以用个bool数组来判断；
// 没有走出边界；
// 横纵坐标的各位数字之和小于 k；
// 最后答案就是所有遍历过的合法的节点个数。

// 时间复杂度
// 每个节点最多只会入队一次，所以时间复杂度不会超过方格中的节点个数。
// 最坏情况下会遍历方格中的所有点，所以时间复杂度就是 O(nm)。
#include<queue>
using namespace std;
class Solution {
public:

    int get_sum(pair<int, int> p) {
        int s = 0;
        while (p.first) {
            s += p.first % 10;
            p.first /= 10;
        }
        while (p.second) {
            s += p.second % 10;
            p.second /= 10;
        }
        return s;
    }
    
    int movingCount(int threshold, int rows, int cols)
    {
        if (!rows || !cols) return 0;
        queue<pair<int,int>> q;
        vector<vector<bool>> st(rows, vector<bool>(cols, false));

        int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};

        int res = 0;
        q.push({0, 0});
        while (q.size()) {
            auto t = q.front();
            q.pop();
            if (st[t.first][t.second] || get_sum(t) > threshold) continue;
            res ++ ;
            st[t.first][t.second] = true;
            for (int i = 0; i < 4; i ++ ) {
                int x = t.first + dx[i], y = t.second + dy[i];
                if (x >= 0 && x < rows && y >= 0 && y < cols) q.push({x, y});
            }
        }

        return res;
    }
};