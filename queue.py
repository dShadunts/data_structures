from stack import Stack


class Queue:
    def __init__(self):
        self.__size = 0
        self.__data = []

    def __len__(self):
        return self.__size

    def enqueue(self, item):
        self.__data.append(item)
        self.__size += 1

    def dequeue(self):
        item = self.__data.pop(0)
        self.__size -= 1
        return item

    def first(self):
        return self.__data[0]

    def is_empty(self):
        return self.__size == 0

    # Reverse first k elements of a queue
    def reverse_k(self, k):
        # check for valid k
        if k < 0 or k > len(self) or self.is_empty():
            return
        s = Stack()

        # Push first k elements to stack  
        for i in range(0, k):
            s.push(self.dequeue())

        # enqueue k elements back, as a result get k elements reversed
        for i in range(0, k):
            self.enqueue(s.pop())

        # move remaining elements to the end of the queue
        for i in range(0, len(self) - k):
            self.enqueue(self.dequeue())

    @classmethod
    def binary_numbers(cls, n):
        q = cls()
        # first binary number
        q.enqueue('1')
        while n > 0:
            n -= 1
            last = q.dequeue()
            print last
            q.enqueue(last + '0')
            q.enqueue(last + '1')
