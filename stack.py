class Stack:
    def __init__(self):
        self.__data = []
        self.__size = 0

    def __len__(self):
        return self.__size

    def push(self, item):
        self.__data.append(item)
        self.__size += 1

    def pop(self):
        item = self.__data.pop()
        self.__size -= 1
        return item

    def top(self):
        return self.__data[-1]

    def is_empty(self):
        return self.__size == 0

    # evaluate postfix expression using stack
    # Postfix expression requires that its operators come after the corresponding operands
    # e.g '22 3 5 * +' is equivalent of 3 * 5 + 22 => eval_postfix('22 3 5 * +') = 37
    @classmethod
    def eval_postfix(cls, expression):
        s = cls()
        for c in expression.split():
            if c.isdigit():
                s.push(int(c))
            else:
                b = s.pop()
                a = s.pop()
                if c == '*':
                    s.push(a * b)
                elif c == '/':
                    s.push(a / b)
                elif c == '+':
                    s.push(a + b)
                elif c == '-':
                    s.push(a - b)
                else:
                    raise ValueError('Illegal postfix expression')
        return s.pop()

    # Check balanced parentheses in an expression
    @classmethod
    def balanced_parentheses(cls, expression):
        s = cls()
        # same type of parentheses have same index
        opening = '([{'
        closing = ')]}'

        for c in expression:
            # encountered opening parentheses => push to the stack
            if c in opening:
                s.push(c)
            # encountered closing parentheses
            elif c in closing:
                # there is no parentheses to match => invalid
                if s.is_empty(): return False
                last = s.pop()
                # are not of the same type => invalid
                if not opening.find(last) == closing.find(c):
                    return False
        # all opening parentheses were matched with closing => valid
        return s.is_empty()

    # sort items using stack
    # time complexity: O(n^2), space usage: O(n)
    def sort(self):
        tmp = Stack()
        while not self.is_empty():
            item = self.pop()
            while not tmp.is_empty() and tmp.top() > item:
                self.push(tmp.pop())
            tmp.push(item)
        self.__data = tmp.__data
        return self
