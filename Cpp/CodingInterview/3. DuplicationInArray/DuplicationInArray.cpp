// 给定一个长度为 n 的整数数组 nums，数组中所有的数字都在 0∼n−1 的范围内。
// 数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
// 请找出数组中任意一个重复的数字。
// 注意：如果某些数字不在 0∼n−1 的范围内，或数组中不包含重复数字，则返回 -1；

// 样例
// 给定 nums = [2, 3, 5, 4, 3, 2, 6, 7]。
// 返回 2 或 3。

// 数组遍历 O(n)
// 首先遍历一遍数组，如果存在某个数不在0到n-1的范围内，则返回-1。
// 下面的算法的主要思想是把每个数放到对应的位置上，即让 nums[i] = i。
// 从前往后遍历数组中的所有数，假设当前遍历到的数是 nums[i]=x，那么：
// 如果x != i && nums[x] == x，则说明 x 出现了多次，直接返回 x 即可；
// 如果nums[x] != x，那我们就把 x 交换到正确的位置上，即 swap(nums[x], nums[i])，
// 交换完之后如果nums[i] != i，则重复进行该操作。
// 由于每次交换都会将一个数放在正确的位置上，所以swap操作最多会进行 n 次，不会发生死循环。
// 循环结束后，如果没有找到任何重复的数，则返回-1。

// 时间复杂度分析
// 每次swap操作都会将一个数放在正确的位置上，最后一次swap会将两个数同时放到正确位置上，
// 一共只有 n 个数和 n 个位置，所以swap最多会进行 n−1 次。所以总时间复杂度是 O(n)。


#include<vector>
using namespace std;
class Solution {
public:
    int duplicateInArray(vector<int>& nums) {
        int n = nums.size();
        for (auto x : nums)
            if (x < 0 || x >= n)
                return -1;
        for (int i = 0; i < n; i ++ ) {
            while (nums[nums[i]] != nums[i]) 
                swap(nums[i], nums[nums[i]]);
            if (nums[i] != i) 
                return nums[i];
        }
        return -1;
    }
};
