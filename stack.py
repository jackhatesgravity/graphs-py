from typing import Any

class Stack:
    def __init__(self):
        self._nodes = []

    def empty(self) -> bool:
        """
        Check if the stack is empty.

        :return: True if empty, False otherwise
        """
        return not self._nodes

    def put(self, x: Any) -> None:
        """
        Push an element onto the stack.

        :param x: The element to push
        :type x: NodeItem
        :return: None
        """
        self._nodes.append(x)

    def get(self) -> Any:
        """
        Pop an element from the stack.

        :return: The popped element
        :rtype: NodeItem
        """
        return self._nodes.pop()

    @property
    def nodes(self):
        return [x for x in self._nodes]