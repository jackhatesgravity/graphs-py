import collections
from typing import Any


class Queue:
    def __init__(self):
        self._nodes = collections.deque()

    def empty(self) -> bool:
        """
        Check if the queue is empty.

        :return: True if empty, False otherwise
        """
        return not self._nodes

    def put(self, x: Any) -> None:
        """
        Enqueue an element into the queue.

        :param x: The element to enqueue
        :type x: NodeItem
        :return: None
        """
        self._nodes.append(x)

    def get(self) -> Any:
        """
        Dequeue an element from the queue.

        :return: The dequeued element
        :rtype: NodeItem
        """
        return self._nodes.popleft()

    @property
    def nodes(self):
        return [x for x in self._nodes]
