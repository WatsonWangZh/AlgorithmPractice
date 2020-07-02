# Given a url startUrl, implement a web crawler to crawl all links that are under the same hostname as startUrl. 
# Your crawler should:
# Start from the page: startUrl
# Call HtmlParser.getUrls(url) to get all urls from a webpage of given url.
# Do not crawl the same link twice.
# Only crawl the links that are under the same hostname as startUrl.
# example.org:8888
# As shown in the example url above, the hostname is example.org. 
# For simplicity sake, you may assume all urls use http protocol without any port specified.

# Example 1:
# Input:
# urls = [
#   "http://news.yahoo.com",
#   "http://news.yahoo.com/news",
#   "http://news.yahoo.com/news/topics/",
#   "http://news.google.com",
#   "http://news.yahoo.com/us"
# ]
# edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
# startUrl = "http://news.yahoo.com/news/topics/"
# Output: [
#   "http://news.yahoo.com",
#   "http://news.yahoo.com/news",
#   "http://news.yahoo.com/news/topics/",
#   "http://news.yahoo.com/us"
# ]
# Explanation:
# Edges show how these urls connect with each other.
# 1. startUrl http://news.yahoo.com/news/topics/ (index 2) links to:
#      -> http://news.yahoo.com/news (index 1)
#      -> http://news.yahoo.com      (index 0). 
# 2. http://news.yahoo.com (index 0) links to:
#      -> http://news.yahoo.com/us   (index 4). 

# Example 2:
# Input: 
# urls = [
#   "http://news.yahoo.com",
#   "http://news.yahoo.com/news",
#   "http://news.yahoo.com/news/topics/",
#   "http://news.google.com"
# ]
# edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]
# startUrl = "http://news.google.com"
# Output: ["http://news.google.com"]
# Explanation: The startUrl links to all other pages that do not share the same hostname.
 
# Constraints:
# 1 <= urls.length <= 1000
# 1 <= urls[i] <= 300
# Hostname labels may contain only the ASCII letters 'a' through 'z' (in a case-insensitive manner), 
# the digits '0' through '9' and the hyphen-minus character ('-'). 
# The hostname may not start or end with the hyphen-minus character ('-'). 
# See:  https://en.wikipedia.org/wiki/Hostname#Restrictions_on_valid_hostnames
# You may assume there're no duplicates in url library.

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        # DFS遍历，每到一个新的链接，获取其hostname
        # 验证startUrl所链接到的hostname与起始hostname是否一致，并验证各部分是否有效
        # 然后查找结果集(以set实现去重效果)，决定是否添加到结果集中。

        def _validate(string):
            if string[0] == '-' or string[-1] == '-':
                return False

            for c in string:
                if not c.isdigit() and not c.islower() and not c == '-':
                    return False
            return True

        def get_host(url):
            without_http = url[7:]
            idx = without_http.find('/')
            return without_http[:(len(without_http) + 1) if idx == -1 else idx]
        
        def validate(host):
            host_parts = host.split('.')
            return all([_validate(host_part) for host_part in host_parts])

        hostname = get_host(startUrl)
        
        if not validate(hostname):
            return []
        
        stack = [startUrl]
        res = set([startUrl])
        while stack:
            url = stack.pop()
            # print(url)
            for _url in htmlParser.getUrls(url):
                h = get_host(_url)
                # print(h)
                if h == hostname and validate(h) and _url not in res:
                    res.add(_url)
                    stack.append(_url)
            
        return list(res)