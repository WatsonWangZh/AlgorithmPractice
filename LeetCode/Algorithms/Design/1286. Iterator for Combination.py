# Design an Iterator class, which has:
# A constructor that takes a string characters of sorted distinct lowercase English letters 
# and a number combinationLength as arguments.
# A function next() that returns the next combination of length combinationLength in lexicographical order.
# A function hasNext() that returns True if and only if there exists a next combination.
 
# Example:
# CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.
# iterator.next(); // returns "ab"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "ac"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "bc"
# iterator.hasNext(); // returns false
 
# Constraints:
# 1 <= combinationLength <= characters.length <= 15
# There will be at most 10^4 function calls per test.
# It's guaranteed that all calls of the function next are valid.

# Hints:
# Generate all combinations as a preprocessing.
# Use bit masking to generate all the combinations.

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        lst = []
        n = len(characters)
        def dfs(path, i):

            if len(path) == combinationLength:
                lst.append(path)
                return
            for j in range(i, n):
                dfs(path + characters[j], j+1)
        dfs('', 0)
        self.lst = lst[::-1]


    def next(self) -> str:
        return self.lst.pop()

    def hasNext(self) -> bool:
        return len(self.lst) > 0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
