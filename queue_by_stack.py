from stack import Stack


# Problem: implement queue using stacks
# Solution: keep two stacks, one for enqueue and one for dequeue
# Each will be pushed and popped from stacks 2 times
# the amortized cost of enqueue: 3.
# the amortized cost of dequeue: 1.
class QueueByStack:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, item):
        self.inbox.push(item)

    def dequeue(self):
        i = self.inbox
        o = self.outbox
        if o.is_empty():
            # if outbox is empty, fill it with values of inbox
            while not i.is_empty():
                o.push(i.pop())
        # top element in the outbox will be the first element in the queue
        return o.pop()

    def is_empty(self):
        return self.inbox.is_empty() and self.outbox.is_empty()
