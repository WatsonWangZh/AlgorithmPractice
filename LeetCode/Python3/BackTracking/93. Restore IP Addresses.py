# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# Example:
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if len(s) < 4 or len(s) > 12:
            return res

        def dfs(res, s, cur, fields):
            # s 待处理字符串
            # cur 已处理字符串
            # fields 已完成块数
            print(cur)
            if fields == 4 and len(s) == 0:
                res.append(cur[1:])
            if fields == 4 or len(s) == 0:
                return
            # 一位数情况
            dfs(res, s[1:], cur+'.'+s[0], fields+1)
            # 两位数情况
            # str(int(s[0:2]))==s[0:2] 控制前缀0
            if s[0] != 0 and len(s) > 1 and str(int(s[0:2]))==s[0:2]:
                dfs(res, s[2:], cur+'.'+s[0:2], fields+1)
                #  三位数情况
            if s[0] != 0 and len(s) > 2 and int(s[0:3]) <= 255 and str(int(s[0:3]))==s[0:3]:
                dfs(res, s[3:], cur+'.'+s[0:3], fields+1)
                
        dfs(res, s, "", 0)
        return res