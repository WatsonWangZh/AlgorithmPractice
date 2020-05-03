// 在字符串中找出第一个只出现一次的字符。
// 如输入"abaccdeff"，则输出b。
// 如果字符串中不存在只出现一次的字符，返回#字符。

// 样例：
// 输入："abaccdeff"
// 输出：'b'

#include<string>
#include<unordered_map>
using namespace std;
class Solution {
public:
    char firstNotRepeatingChar(string s) {
        unordered_map<char, int> count;
        for (auto c : s) count[c]++;
        char res = '#';
        for(auto c : s)
            if (count[c] == 1){
                res = c;
                break;
            }
        return res;
    }
};

// 请实现一个函数用来找出字符流中第一个只出现一次的字符。
// 例如，当从字符流中只读出前两个字符”go”时，第一个只出现一次的字符是’g’。
// 当从该字符流中读出前六个字符”google”时，第一个只出现一次的字符是’l’。
// 如果当前字符流没有存在出现一次的字符，返回#字符。

// 样例
// 输入："google"
// 输出："ggg#ll"
// 解释：每当字符流读入一个字符，就进行一次判断并输出当前的第一个只出现一次的字符。

#include<queue>
#include<unordered_map>
class Solution{
public:

    unordered_map<char, int> count;
    queue<char> q;
    //Insert one char from stringstream
    void insert(char ch){
        if (++ count[ch] > 1){
            while(q.size() && count[q.front()] > 1) q.pop();
        }
        else q.push(ch);
    }
    //return the first appearence once char in current stringstream
    char firstAppearingOnce(){
        if(q.empty()) return '#';
        return q.front();
    }
};