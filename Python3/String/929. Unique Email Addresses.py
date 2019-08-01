# Every email consists of a local name and a domain name, separated by the @ sign.
# For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

# Besides lowercase letters, these emails may contain '.'s or '+'s.

# If you add periods ('.') between some characters in the local name part of an email address, 
# mail sent there will be forwarded to the same address without dots in the local name.  
# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  
# (Note that this rule does not apply for domain names.)

# If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. 
# This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  
# (Again, this rule does not apply for domain names.)

# It is possible to use both of these rules at the same time.

# Given a list of emails, we send one email to each address in the list.  
# How many different addresses actually receive mails? 

# Example 1:
# Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
 
# Note:
# 1 <= emails[i].length <= 100
# 1 <= emails.length <= 100
# Each emails[i] contains exactly one '@' character.
# All local and domain names are non-empty.
# Local names do not start with a '+' character.

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # 哈希表，字符串处理 O(n)
        # 遍历emails中的每个邮箱地址，然后依次进行如下操作：
        # 分别找出用户名和域名；
        # 从前往后遍历用户名的每个字符，如果遇到'+'，则直接截断；如果遇到'.'，则忽略该字符；
        # 将新用户名和域名重新组合，再插入哈希表中；
        # 最终哈希表中不同元素的个数就是答案。
        # 时间复杂度分析：'emails'中的每个邮箱地址只会遍历2遍，且哈希表的插入和查找的时间复杂度均是 O(L)，L是字符串长度。
        # 所以总时间复杂度是 O(n)，n 表示字符串总长度。
        
        email_set = set()
        for email in emails:
            local, domain = email.split("@")
            cleaned_local = local.split('+')[0].replace('.','')
            email_set.add(cleaned_local + '@' + domain)
        return len(email_set)
        