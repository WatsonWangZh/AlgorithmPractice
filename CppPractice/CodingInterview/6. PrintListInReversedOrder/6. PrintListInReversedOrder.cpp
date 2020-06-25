// 输入一个链表的头结点，按照 从尾到头 的顺序返回节点的值。
// 返回的结果用数组存储。

// 样例
// 输入：[2, 3, 5]
// 返回：[5, 3, 2]

// 遍历链表 O(n)
// 单链表只能从前往后遍历，不能从后往前遍历。
// 因此我们先从前往后遍历一遍输入的链表，将结果记录在答案数组中。
// 最后再将得到的数组逆序即可。
// 时间复杂度分析
// 链表和答案数组仅被遍历了常数次，所以总时间复杂度是 O(n)。

#include<vector>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };
 
class Solution {
public:
    vector<int> printListReversingly(ListNode* head) {
        vector<int> res;
        while (head) {
            res.push_back(head->val);
            head = head->next;
        }
        return vector<int>(res.rbegin(), res.rend());
    }
};
