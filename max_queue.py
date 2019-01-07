from collections import deque


class MaxQueue:
    def __init__(self):
        self.__size = 0
        self.__data = []
        self.__max_values = deque()

    def __len__(self):
        return self.__size

    def enqueue(self, value):
        # delete all the items in max_values which are less than the value we add
        # as current element will stay in the queue longer
        if not self.is_empty():
            while self.__max_values and self.__max_values[-1] < value:
                self.__max_values.pop()
        self.__data.append(value)
        self.__max_values.append(value)
        self.__size += 1

    def dequeue(self):
        item = self.__data.pop(0)
        if item == self.max():
            self.__max_values.popleft()
        self.__size -= 1
        return item

    def first(self):
        return self.__data[0]

    def is_empty(self):
        return self.__size == 0

    # front of the deque is max
    def max(self):
        return self.__max_values[0]
