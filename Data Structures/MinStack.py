'''
Design a stack that supports push, pop, top,
and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

'''

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.normalStack = []
        self.minimal = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.normalStack) == 0:
          self.minimal = x
          self.normalStack.append(x)
          return

        if x >= self.minimal:
          self.normalStack.append(x)
        else:
          self.normalStack.append(2 * x - self.minimal)
          self.minimal = x

    def pop(self):
        """
        :rtype: None
        """
        removeValue = self.normalStack[-1]

        if removeValue>= self.minimal:
          return self.normalStack.pop()
        else:
          temp = self.normalStack.pop()
          currentMinimal = self.minimal
          self.minimal = 2 * self.minimal - temp
          return currentMinimal





    def top(self):
        """
        :rtype: int
        """
        if self.normalStack[-1] >= self.minimal:
          return self.normalStack[-1]
        else:
          return self.minimal


    def getMin(self):
        """
        :rtype: int
        """
        return self.minimal
