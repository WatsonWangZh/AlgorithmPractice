# Design a stack that supports push, pop, top, 
# and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
import sys
class MinStack:
    # 最小栈相较于普通栈，可以实时保存当前栈中的最小值，故需设置min变量保存更新。
    # 边界条件：push时，若当前元素比最小值还小，则需更新最小值，且保存进栈前的最小值供下一次比较；
    #         pop时，若pop的元素为最小值，则需把最小值更新为次小值。
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = sys.maxsize

    def push(self, x: int) -> None:
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min:
            self.min = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()