class LinkedList:

    class Node:
        """
        A basic Node class used to store data in some kind of higher data structure.
        For now, I'm allowing data to be None, but that might change.
        """

        def __str__(self):
            return f"{{ Data: {self.data}, Next: {self.next} }}"

        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __str__(self):
        return (f"head: {self.head.data if self.head is not None else None},"
                f"\ntail: {self.tail.data if self.tail is not None else None},"
                f"\ncount: {self.count}")

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def empty(self):
        return self.count == 0

    def push(self, data):
        """
        Create and push a new node to the top of the list.
        :param data: Data to store in the new node.
        :return: The newly created node.
        """
        # if data is None:
        #     raise Exception("Data is empty!")  # Does this crash out the way I expect it to?
        new_node = self.Node(data)
        if not self.empty():
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.count += 1
        return new_node

    def pop(self):
        if not self.empty():
            old_tail = self.tail
            # Handle case when more than one node left in the list.
            if self.tail.prev is not None:
                self.tail = self.tail.prev
                self.tail.next = None
            # Handle the case when removing the last node in the list.
            else:
                self.head = None
                self.tail = None
            self.count -= 1
            return old_tail
        else:
            raise Exception("LinkedList is empty!")