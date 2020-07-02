# Design and implement a data structure for a compressed string iterator. 
# It should support the following operations: next and hasNext.
# The given compressed string will be in the form of each letter 
# followed by a positive integer representing the number of this letter existing in the original uncompressed string.
# next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
# hasNext() - Judge whether there is any letter needs to be uncompressed.

# Note:
# Please remember to RESET your class variables declared in StringIterator, 
# as static/class variables are persisted across multiple test cases. Please see here for more details.

# Example:
# StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
# iterator.next(); // return 'L'
# iterator.next(); // return 'e'
# iterator.next(); // return 'e'
# iterator.next(); // return 't'
# iterator.next(); // return 'C'
# iterator.next(); // return 'o'
# iterator.next(); // return 'd'
# iterator.hasNext(); // return true
# iterator.next(); // return 'e'
# iterator.hasNext(); // return false
# iterator.next(); // return ' '

# https://leetcode.com/problems/design-compressed-string-iterator/solution/
# Demand-Computation
class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.string = compressedString
        self.cnt = 0
        self.char = ""

    def next(self):
        """
        :rtype: str
        """
        if self.cnt > 0:
            self.cnt -= 1
            return self.char
        elif len(self.string) == 0:
            return ' '
        else:
            self.char = self.string[0]
            self.string = self.string[1:]
            cnt = ""
            while len(self.string) > 0 and self.string[0].isdigit():
                cnt += self.string[0]
                self.string = self.string[1:]
            self.cnt = int(cnt)
            return self.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cnt > 0 or len(self.string) > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()