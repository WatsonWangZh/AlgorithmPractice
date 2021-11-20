# Implement a trie with insert, search, and startsWith methods.
# Example:
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree={
            "root":{}
        }
        # print(self.tree)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.tree["root"]
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr["eow"] = "Y"
        # print(self.tree)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.tree["root"]
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        if "eow" not in curr or curr["eow"] != "Y":
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.tree["root"]
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)