class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.__size = 0

    def add_to_start(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.__size += 1

    def remove(self, data):
        h = self.head
        # remove from start
        if h and h.data == data:
            self.head = h.next
            self.__size -= 1
            return

        # find the node to be removed from the middle
        while (h is not None):
            if h.data == data:
                break
            prev = h
            h = h.next

        if (h is not None):
            self.__size -= 1
            prev.next = h.next

    # Reverse a linked list
    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    # Detect if linked list has a loop
    def has_loop(self):
        hare = self.head
        tortoise = self.head

        while hare and hare.next and tortoise:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                return True

        return False

    # get the nth element from the end
    def nth_from_end(self, n):
        if n > self.__size:
            return
        curr = self.head
        for i in range(0, self.__size - n):
            curr = curr.next
        return curr

    # Remove duplicates from a linked list
    def remove_duplicates(self):
        # check for duplicates every element starting from head
        curr = self.head
        while curr and curr.next:
            # candidate duplicate node
            node = curr
            while node.next:
                # found a duplicate -> remove
                if curr.data == node.next.data:
                    node.next = node.next.next
                else:
                    node = node.next
            # removed all duplicates for current -> move to next
            curr = curr.next
