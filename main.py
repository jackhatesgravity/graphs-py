class Node:
    def __str__(self):
        return f"{{ Data: {self.data}, Next: {self.next} }}"

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __str__(self):
        return f"head: {self.head.data},\ntail: {self.tail.data},\ncount: {self.count}"

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
        if data is None:
            raise Exception("Data is empty!") # Does this crash out the way I expect it to?
        new_node = Node(data)
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
            self.tail = self.tail.prev
            self.tail.next = None
            self.count -= 1
            return old_tail
        else:
            raise Exception("LinkedList is empty!")


def main():
    new_list = LinkedList()
    new_list.push(1)
    new_list.push(2)
    new_list.push(3)

    print(new_list)


if __name__ == "__main__":
    main()
