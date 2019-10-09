# Design an in-memory file system to simulate the following functions:

# ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. 
# If it is a directory path, return the list of file and directory names in this directory. 
# Your output (file and directory names together) should in lexicographic order.

# mkdir: Given a directory path that does not exist, you should make a new directory according to the path. 
# If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

# addContentToFile: Given a file path and file content in string format. 
# If the file doesn't exist, you need to create that file containing given content. 
# If the file already exists, you need to append given content to original content. This function has void return type.

# readContentFromFile: Given a file path, return its content in string format.

# Example:
# Input: 
# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
# [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
# Output:
# [null,[],null,null,["a"],"hello"]

# Note:
# You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
# You can assume that all operations will be passed valid parameters 
# and users will not attempt to retrieve file content or list a directory or file that does not exist.
# You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.

class FileSystem(object):

    def __init__(self):
        self.dirs = {'/':[]}
        self.files = {}

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        if path not in self.dirs:
            self.mkdir(path)
        return sorted(self.dirs[path])

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        curr_p = ''
        prev_p = '/'
        path = list(filter(None, path.split('/')))
        # path = list(path[1:].split('/'))
        # print(path)
        for p in path:
            curr_p += '/' + p
            if p not in self.dirs[prev_p]:
                self.dirs[prev_p].append(p)
            if curr_p not in self.dirs:
                self.dirs.setdefault(curr_p, [])
            prev_p = curr_p

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        self.mkdir(filePath)
        # for '/a/b/c' -> split ['','a','b','c'] ,that '' doesn't exsist in keys()
        path = list(filter(None, filePath.split('/')))
        # path = list(filePath[1:].split('/'))
        # print(path)
        if filePath not in self.files:
            self.files[filePath] = content
            self.dirs[filePath].append(path[-1])
        else:
            self.files[filePath] += content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        return self.files[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)